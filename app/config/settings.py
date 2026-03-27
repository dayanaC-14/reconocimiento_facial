import os
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    DEBUG = os.getenv("DEBUG")
    ENV = os.getenv("ENV")

# Crear instancia
settings = Settings()