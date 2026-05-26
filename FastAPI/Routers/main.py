from fastapi import FastAPI
from routers.users import router as users_router

app = FastAPI()
app.include_router(users_router)        # Acceder mediante http://localhost:8000/users/