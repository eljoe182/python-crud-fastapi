from typing import Optional
from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float
    is_active: bool


class ProductStoreSchema(BaseModel):
    name: str
    description: str
    price: float
    is_active: bool


class ProductUpdateSchema(BaseModel):
    name: str | None = None
    description: str | None = None 
    price: float | None = None
    is_active: bool | None = None
