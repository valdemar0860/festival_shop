from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas.product import Product as ProductSchema
from app.db.models.product import Product
from app.db.models.tag import Tag
from app.db.session import get_db
from app.services.product_service import create_product
from app.schemas.product import ProductCreate

router = APIRouter()


@router.get("/", response_model=List[ProductSchema])
def get_products(
    tag_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Product)
    if tag_id:
        query = query.join(Product.tags).filter(Tag.id == tag_id)
    return query.all()



@router.post("/", response_model=ProductSchema)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

