from fastapi import FastAPI

from app.auth.auth_routes import auth_router
from app.routes.protected_routes import protected_router
# add cors middleware
from fastapi.middleware.cors import CORSMiddleware

origins = ["*",]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(protected_router)


@app.get("/")
def read_root():
    return {"message": "API is running"}
