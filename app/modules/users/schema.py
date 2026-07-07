from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario único")
    email: EmailStr = Field(..., description="Correo electrónico válido")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Contraseña segura de acceso")

class UserResponse(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }