from fastapi import APIRouter
from .schema import UserCreate

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):
    return{
        "mesage": "Usuario creado exitosamente",
        "user": user 
    }