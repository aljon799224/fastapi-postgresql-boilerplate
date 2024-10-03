import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import PostgresDsn

load_dotenv()

class Settings:
    API_PREFIX = '/api/v1'
    SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

settings = Settings()
