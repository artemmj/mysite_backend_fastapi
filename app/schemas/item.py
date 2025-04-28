from pydantic import BaseModel
from typing import Optional


# Базовые схемы для предметов
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

# Схема для создания предмета
class ItemCreate(ItemBase):
    pass

# Схема для обновления предмета
class ItemUpdate(ItemBase):
    name: Optional[str] = None

# Схема для ответа (с владельцем)
class ItemResponse(ItemBase):
    id: int
    owner_email: str

    class Config:
        from_attributes = True
