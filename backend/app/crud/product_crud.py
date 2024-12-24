from sqlalchemy.orm import Session
from app.db.models.product import Product
from app.db.models.tag import Tag
from app.schemas.product import ProductCreate

def create_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        image_url=product.image_url,
        category_id=product.category_id,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    if product.tags:
        tags = db.query(Tag).filter(Tag.id.in_(product.tags)).all()
        db_product.tags.extend(tags)
        db.commit()

    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, updates: dict):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    for key, value in updates.items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return True
