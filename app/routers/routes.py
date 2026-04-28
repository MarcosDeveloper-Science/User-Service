from fastapi import APIRouter

from app.schemas.schemas import UserCreate, UserResponse
from app.services.user_service import create_user_service, list_users_service

# Cria Grupo de Rotas
router = APIRouter(prefix="/users", tags=["Users"])


# Rota Post /users
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return create_user_service(user.name)


# Rota Get /users
@router.get("/", response_model=list[UserResponse])
def list_users():
    return list_users_service()
