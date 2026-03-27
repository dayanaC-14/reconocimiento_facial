from pydantic import BaseModel

class UserCreate(BaseModel):
    nombre: str
    tipo_rostro: str