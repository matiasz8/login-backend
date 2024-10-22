from fastapi import APIRouter, HTTPException

from app.auth.auth_handler import create_access_token
from app.schemas.user import User

auth_router = APIRouter()

users_db = {"testuser": {"username": "testuser", "password": "testpass"}}


@auth_router.post("/login")
def login(user: User):
    if (
        user.username in users_db
        and users_db[user.username]["password"] == user.password
    ):
        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(status_code=401, detail="Invalid username or password")
