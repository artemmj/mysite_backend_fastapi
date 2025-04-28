from pydantic import BaseModel, EmailStr


# Схема для создания пользователя
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Схема для ответа (без пароля)
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # Для работы с ORM объектами

# Схема для аутентификации
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
