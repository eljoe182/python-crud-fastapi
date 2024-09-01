from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import conn
from models.ProductModel import product_model
from schemas.ProductSchema import ProductStoreSchema, ProductSchema, ProductUpdateSchema

router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/get-all")
def get_all():
    result = conn.execute(product_model.select()).mappings().all()

    return result


@router.post("/store")
def store(product: ProductStoreSchema):
    new_product = {
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "is_active": product.is_active,
    }
    result = conn.execute(
        product_model.insert()
        .values(new_product)
        .return_defaults(
            product_model.c.name,
            product_model.c.description,
            product_model.c.price,
            product_model.c.is_active,
        )
    )
    conn.commit()
    product_stored = (
        conn.execute(
            product_model.select().where(product_model.c.id == result.lastrowid)
        )
        .mappings()
        .first()
    )
    return product_stored


@router.get("/get-by-id/{id}")
def get_by_id(id: int):
    result = (
        conn.execute(product_model.select().where(product_model.c.id == id))
        .mappings()
        .first()
    )
    return result


@router.put("/update/{id}")
def update(id: int, product: ProductUpdateSchema):
    product_updated = {
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "is_active": product.is_active,
    }

    conn.execute(
        product_model.update().where(product_model.c.id == id).values(product_updated)
    )
    conn.commit()

    result = (
        conn.execute(product_model.select().where(product_model.c.id == id))
        .mappings()
        .first()
    )
    return result


@router.delete("/delete/{id}")
def delete(id: int):
    conn.execute(product_model.delete().where(product_model.c.id == id))
    conn.commit()
    return {"product": "deleted"}
