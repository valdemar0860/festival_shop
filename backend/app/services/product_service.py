from sqlalchemy.orm import Session
from app.crud.product_crud import create_product, get_product
from app.schemas.product import ProductCreate
from app.db.models.product import Product

def create_product(db: Session, product_data: ProductCreate):
    existing_product = db.query(Product).filter(Product.name == product_data.name).first()
    if existing_product:
        raise ValueError(f"Продукт із назвою '{product_data.name}' вже існує!")
    
    new_product = create_product(db, product_data)
    return new_product
