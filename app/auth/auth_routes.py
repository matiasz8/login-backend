import hashlib
from fastapi import APIRouter, HTTPException

from app.auth.auth_handler import create_access_token
from app.schemas.user import User

auth_router = APIRouter()

users_db = [{"email": "test@mail.com", "hashed_password": hashlib.sha256("test".encode('utf-8')).hexdigest()}]

@auth_router.post("/login")
def login(user: User):
    for user_db in users_db:
        if user_db["email"] == user.email:
            hashed_password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
            if hashed_password == user_db["hashed_password"]:
                token = create_access_token({"sub": user.email})
                return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid email or password")
