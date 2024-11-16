from fastapi import FastAPI
from app.db.models.base import Base
from app.db.session import engine
from app.api.v1.endpoints import products 

app = FastAPI()

# Створення таблиць у базі даних
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
    
app.include_router(products.router, prefix="/api/v1", tags=["products"])
