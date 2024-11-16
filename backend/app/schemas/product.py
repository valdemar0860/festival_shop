from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str

    class Config:
        orm_mode = True
