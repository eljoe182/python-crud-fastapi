from fastapi import APIRouter
from app.controllers.ProductController import ProductController
from domain.infrastructure.schemas.ProductSchema import (
    ProductStoreSchema,
    ProductUpdateSchema,
)

router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/get-all")
def get_all():
    controller = ProductController()
    return controller.get_all_products()


@router.post("/store")
def store(product: ProductStoreSchema):
    controller = ProductController()
    return controller.store_product(product)


@router.get("/get-by-id/{id}")
def get_by_id(id: int):
    controller = ProductController()
    return controller.get_by_id_product(id)


@router.put("/update/{id}")
def update(id: int, product: ProductUpdateSchema):
    controller = ProductController()
    return controller.update_product(id, product)


@router.delete("/delete/{id}")
def delete(id: int):
    controller = ProductController()
    return controller.delete_product(id)
