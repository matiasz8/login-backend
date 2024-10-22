from fastapi import APIRouter, Depends

from app.auth.auth_handler import verify_token

protected_router = APIRouter()


@protected_router.get("/protected")
def protected_route(current_user: dict = Depends(verify_token)):
    return {"message": f"Welcome {current_user['sub']}, you are authenticated!"}
