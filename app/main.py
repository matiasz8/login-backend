from fastapi import FastAPI

from app.auth.auth_routes import auth_router
from app.routes.protected_routes import protected_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(protected_router)


@app.get("/")
def read_root():
    return {"message": "API is running"}
