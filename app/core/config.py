import os
from pydantic import Field

class Settings:
    SECRET_KEY: str = Field(alias="SECRET_KEY", default="mysecretkey")
    title: str = Field(alias="APP_TITLE", default="Login's API")
    version: str = Field(alias="APP_VERSION", default="0.0.1")
    stage: str = Field(alias="STAGE", default="local")

settings = Settings()
