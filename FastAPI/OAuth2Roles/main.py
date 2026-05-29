from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, PAut2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
import bcrypt