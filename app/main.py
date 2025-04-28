from fastapi import FastAPI
from app.routers import auth, items
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/api")
app.include_router(items.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Hello World"}
