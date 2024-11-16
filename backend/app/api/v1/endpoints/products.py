from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import session
from app.db.models.product import Product
from app.schemas.product import ProductResponse
from typing import List

router = APIRouter()

@router.get("/products", response_model=List[ProductResponse])
def get_products(db: Session = Depends(session.get_db)):
    return db.query(Product).all()
