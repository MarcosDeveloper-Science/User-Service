from pydantic_settings import BaseSettings


# classe que le variaveis do .env
class Settings(BaseSettings):
    app_name: str = "User Service"  # nome da Api
    debug: bool = True  # modo debug

    class Config:
        env_file = ".envs/.env"  # caminho do env


# objet global de Configuraçao
settings = Settings()
