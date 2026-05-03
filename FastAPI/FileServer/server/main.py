import os
import base64
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel


'''
Prueba desde bash:

1. Obtener token.

curl -X POST http://localhost:8000/auth/token \
  -d "username=admin&password=secret123"

2. Enviar archivo.

FILE_B64=$(base64 -w 0 mi_archivo.pdf)

curl -X POST http://localhost:8000/files/upload \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d "{
    \"filename\": \"mi_archivo.pdf\",
    \"content_type\": \"application/pdf\",
    \"file_base64\": \"$FILE_B64\"
  }"
'''

# ──────────────────────────────────────────────
# Configuración
# ──────────────────────────────────────────────
SECRET_KEY = "cambia-esta-clave-secreta-en-produccion"  # openssl rand -hex 32
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# ──────────────────────────────────────────────
# Utilidades de contraseña y JWT
# ──────────────────────────────────────────────
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Base de datos de usuarios simulada
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("secret123"),
        "disabled": False,
    }
}

# ──────────────────────────────────────────────
# Modelos Pydantic
# ──────────────────────────────────────────────
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class FileUploadRequest(BaseModel):
    filename: str           # Nombre original del archivo, ej: "documento.pdf"
    content_type: str       # MIME type, ej: "application/pdf"
    file_base64: str        # Contenido del archivo codificado en base64

class FileUploadResponse(BaseModel):
    message: str
    saved_filename: str
    original_filename: str
    size_bytes: int
    path: str

# ──────────────────────────────────────────────
# Lógica de autenticación
# ──────────────────────────────────────────────
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: dict, username: str) -> Optional[UserInDB]:
    if username in db:
        return UserInDB(**db[username])
    return None

def authenticate_user(db: dict, username: str, password: str) -> Optional[UserInDB]:
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(fake_users_db, token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_active_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user

# ──────────────────────────────────────────────
# Aplicación FastAPI
# ──────────────────────────────────────────────
app = FastAPI(
    title="Servicio de carga de archivos",
    description="API con autenticación JWT para guardar archivos en base64",
    version="1.0.0",
)

# ── Auth ──────────────────────────────────────
@app.post("/auth/token", response_model=Token, tags=["Autenticación"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Obtiene un token JWT. Usa username=admin / password=secret123 para probar."""
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": token, "token_type": "bearer"}

# ── Archivos ──────────────────────────────────
@app.post("/files/upload", response_model=FileUploadResponse, tags=["Archivos"])
async def upload_file(
    payload: FileUploadRequest,
    current_user: User = Depends(get_active_user),
):
    """
    Recibe un archivo codificado en base64, lo decodifica y lo guarda en el servidor.

    - **filename**: nombre original del archivo (incluye extensión)
    - **content_type**: tipo MIME del archivo
    - **file_base64**: contenido del archivo en base64

    Requiere autenticación JWT (Bearer token).
    """
    # Decodificar base64
    try:
        # Eliminar prefijo data URI si existe, ej: "data:application/pdf;base64,..."
        raw_b64 = payload.file_base64
        if "," in raw_b64:
            raw_b64 = raw_b64.split(",", 1)[1]
        file_bytes = base64.b64decode(raw_b64)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="El contenido base64 no es válido",
        )

    # Generar nombre único para evitar colisiones
    extension = Path(payload.filename).suffix or ""
    unique_name = f"{uuid.uuid4().hex}{extension}"
    destination = UPLOAD_DIR / unique_name

    # Guardar en disco
    destination.write_bytes(file_bytes)

    return FileUploadResponse(
        message="Archivo guardado exitosamente",
        saved_filename=unique_name,
        original_filename=payload.filename,
        size_bytes=len(file_bytes),
        path=str(destination),
    )

@app.get("/files", tags=["Archivos"])
async def list_files(current_user: User = Depends(get_active_user)):
    """Lista todos los archivos guardados en el servidor."""
    files = [
        {
            "filename": f.name,
            "size_bytes": f.stat().st_size,
            "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
        }
        for f in UPLOAD_DIR.iterdir()
        if f.is_file()
    ]
    return {"files": files, "total": len(files)}

@app.get("/", tags=["Health"])
async def root():
    return {"status": "ok", "docs": "/docs"}
