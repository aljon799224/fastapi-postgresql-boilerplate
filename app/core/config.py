"""Config."""

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Settings Class."""

    API_PREFIX = "/api/v1"
    SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


settings = Settings()
