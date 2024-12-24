from typing import List, Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[int] = None 

class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    subcategories: List["Category"] = [] 

    class Config:
        orm_mode = True
