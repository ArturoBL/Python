"""
Cliente Python para subir archivos al servicio FastAPI con JWT.

Uso:
    python cliente.py archivo.pdf
    python cliente.py imagen.png --url http://mi-servidor.com
"""

import argparse
import base64
import mimetypes
import sys
from pathlib import Path

import requests

# ──────────────────────────────────────────────
# Configuración por defecto
# ──────────────────────────────────────────────
BASE_URL = "http://localhost:8000"
USERNAME = "admin"
PASSWORD = "secret123"


# ──────────────────────────────────────────────
# 1. Autenticación — obtiene el JWT
# ──────────────────────────────────────────────
def obtener_token(base_url: str, username: str, password: str) -> str:
    print(f"🔐 Autenticando como '{username}'...")
    response = requests.post(
        f"{base_url}/auth/token",
        data={"username": username, "password": password},
        timeout=10,
    )
    if response.status_code != 200:
        print(f"❌ Error de autenticación [{response.status_code}]: {response.text}")
        sys.exit(1)

    token = response.json()["access_token"]
    print("✅ Token obtenido correctamente.\n")
    return token


# ──────────────────────────────────────────────
# 2. Codifica el archivo en base64
# ──────────────────────────────────────────────
def leer_archivo_base64(ruta: Path) -> tuple[str, str]:
    if not ruta.exists():
        print(f"❌ Archivo no encontrado: {ruta}")
        sys.exit(1)

    content_type, _ = mimetypes.guess_type(str(ruta))
    content_type = content_type or "application/octet-stream"

    file_bytes = ruta.read_bytes()
    file_b64 = base64.b64encode(file_bytes).decode("utf-8")

    size_kb = len(file_bytes) / 1024
    print(f"📄 Archivo  : {ruta.name}")
    print(f"   Tipo     : {content_type}")
    print(f"   Tamaño   : {size_kb:.1f} KB")
    print(f"   Base64   : {len(file_b64)} caracteres\n")

    return file_b64, content_type


# ──────────────────────────────────────────────
# 3. Sube el archivo al servidor
# ──────────────────────────────────────────────
def subir_archivo(base_url: str, token: str, ruta: Path) -> dict:
    file_b64, content_type = leer_archivo_base64(ruta)

    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "filename": ruta.name,
        "content_type": content_type,
        "file_base64": file_b64,
    }

    print("📤 Subiendo archivo...")
    response = requests.post(
        f"{base_url}/files/upload",
        json=payload,
        headers=headers,
        timeout=60,
    )

    if response.status_code != 200:
        print(f"❌ Error al subir [{response.status_code}]: {response.text}")
        sys.exit(1)

    resultado = response.json()
    print("✅ Archivo subido exitosamente.")
    print(f"   Nombre guardado : {resultado['saved_filename']}")
    print(f"   Tamaño          : {resultado['size_bytes']} bytes")
    print(f"   Ruta en servidor: {resultado['path']}\n")
    return resultado


# ──────────────────────────────────────────────
# 4. (Opcional) Lista los archivos del servidor
# ──────────────────────────────────────────────
def listar_archivos(base_url: str, token: str) -> None:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{base_url}/files", headers=headers, timeout=10)

    if response.status_code != 200:
        print(f"❌ Error al listar [{response.status_code}]: {response.text}")
        return

    data = response.json()
    archivos = data["files"]
    print(f"📂 Archivos en el servidor ({data['total']} total):")
    if not archivos:
        print("   (vacío)")
    for f in archivos:
        print(f"   • {f['filename']}  —  {f['size_bytes']} bytes  —  {f['modified']}")


# ──────────────────────────────────────────────
# Punto de entrada
# ──────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(description="Cliente para subir archivos en base64.")
    parser.add_argument("archivo", help="Ruta del archivo a subir")
    parser.add_argument("--url", default=BASE_URL, help=f"URL base del servidor (default: {BASE_URL})")
    parser.add_argument("--user", default=USERNAME, help="Nombre de usuario")
    parser.add_argument("--password", default=PASSWORD, help="Contraseña")
    parser.add_argument("--listar", action="store_true", help="Listar archivos del servidor al finalizar")
    args = parser.parse_args()

    ruta = Path(args.archivo)

    print("=" * 50)
    print("  Cliente de carga de archivos (Base64 + JWT)")
    print("=" * 50 + "\n")

    token = obtener_token(args.url, args.user, args.password)
    subir_archivo(args.url, token, ruta)

    if args.listar:
        listar_archivos(args.url, token)


if __name__ == "__main__":
    main()
