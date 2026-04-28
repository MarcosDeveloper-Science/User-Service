from pydantic import BaseModel


# Entrada da Api (Cria usuario)
class UserCreate(BaseModel):
    name: str


# Saida da api
class UserResponse(BaseModel):
    id: int
    name: str
