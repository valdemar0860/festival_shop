from sqlalchemy import Column, Integer, ForeignKey, Table
from .base import Base


product_tags = Table(
    "product_tags",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)