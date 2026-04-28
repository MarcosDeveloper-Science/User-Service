from fastapi import FastAPI

from app.core.config import settings
from app.routers.routes import router

# cria aplicação
app = FastAPI(title=settings.app_name, debug=settings.debug)

# registra rotas
app.include_router(router)
