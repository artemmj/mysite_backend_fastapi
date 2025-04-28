from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


# Создание движка для подключения к БД
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # Только для SQLite
)

# Фабрика сессий с настройками
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    """Генератор сессий для Dependency Injection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
