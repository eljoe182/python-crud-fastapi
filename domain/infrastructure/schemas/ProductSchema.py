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
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    is_active: Optional[bool]
