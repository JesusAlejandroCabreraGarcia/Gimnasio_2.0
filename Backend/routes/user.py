from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = []

#userModel
class model_user(BaseModel):
    id:str
    usuario:str
    contrasena: str
    created_at:datetime = datetime.now()
    estatus:bool=False


@user.get('/')

def bienvenida():
    return 'Bienvenido al sistema'


@user.get('/users')

def get_usuarios():
    return users


@user.post('/users')

def save_usuarios(insert_users:model_user):
    users.append(insert_users)
    #print(insert_users)
    return "Datos guardados"