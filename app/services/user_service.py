from app.db.database import fake_db


# logica de criar usuario
def create_user_service(name: str):

    # cria usuario com id automatico

    user = {"id": len(fake_db) + 1, "name": name}

    # salva no "banco"
    fake_db.append(user)

    return user


# Lgica de Listar usuarios
def list_users_service():
    return fake_db
