from fastapi import APIRouter, Depends
from app.injection_dependencies.ProductInjectionImpl import ProductInjectionImpl
from context.products.domain.schemas.ProductSchema import (
    ProductStoreSchema,
    ProductUpdateSchema,
)

router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/get-all")
def get_all():
    return ProductInjectionImpl.product_get_all_impl().run()


@router.post("/store")
def store(product: ProductStoreSchema):
    return ProductInjectionImpl.product_store_impl().run(product)


@router.get("/get-by-id/{id}")
def get_by_id(id: int):
    return ProductInjectionImpl.product_find_by_id_impl().run(id)


@router.put("/update/{id}")
def update(id: int, product: ProductUpdateSchema | None = None):
    return ProductInjectionImpl.product_update_impl().run(id, product)


@router.delete("/delete/{id}")
def delete(id: int):
    return ProductInjectionImpl.product_delete_impl().run(id)
