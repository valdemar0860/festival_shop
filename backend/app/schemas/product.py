from pydantic import BaseModel
from typing import List, Optional
from .tag import Tag
from .category import Category



class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    category_id: int

class ProductCreate(ProductBase):
    tags: List[int] = []  

class Product(ProductBase):
    id: int
    category: Category  
    tags: List[Tag] = []  

    class Config:
        orm_mode = True
