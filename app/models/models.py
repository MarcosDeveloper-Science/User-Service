from pydantic import BaseModel

# Modelo interno (estrutura do dado)


class User(BaseModel):
    id: int
    name: str
