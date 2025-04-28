from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.core.config import settings
from app.schemas.item import ItemResponse

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return email

@router.get("/items/", response_model=list[ItemResponse])
async def read_items(current_user: str = Depends(get_current_user)):
    # Тестовые данные
    return [
        {"id": 1, "name": "Item 1", "owner": current_user},
        {"id": 2, "name": "Item 2", "owner": current_user}
    ]
