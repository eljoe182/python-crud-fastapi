from ..persistence.mysql.Client import MySQLClient
from .entities.ProductEntity import ProductEntity
from ..schemas.ProductSchema import ProductStoreSchema, ProductUpdateSchema


class ProductRepository:
    def __init__(self, client: MySQLClient):
        self.conn = client.get_engine().connect()
        self.product_entity = ProductEntity(client).get_table()

    def get_all(self):
        query = self.product_entity.select()
        result = self.conn.execute(query).mappings().all()
        return result

    def store(self, product: ProductStoreSchema):
        new_product = {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "is_active": product.is_active,
        }
        query = self.product_entity.insert().values(new_product)
        result = self.conn.execute(query)
        self.conn.commit()

        query = self.product_entity.select().where(
            self.product_entity.c.id == result.lastrowid
        )
        result = self.conn.execute(query).mappings().first()

        return result

    def get_by_id(self, id: int):
        query = self.product_entity.select().where(self.product_entity.c.id == id)
        result = self.conn.execute(query).mappings().first()
        return result

    def update(self, id: int, product: ProductUpdateSchema):
        update_product = {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "is_active": product.is_active,
        }
        query = (
            self.product_entity.update()
            .where(self.product_entity.c.id == id)
            .values(update_product)
        )
        result = self.conn.execute(query)
        self.conn.commit()

        query = self.product_entity.select().where(self.product_entity.c.id == id)
        result = self.conn.execute(query).mappings().first()

        return result

    def delete(self, id: int):
        query = self.product_entity.delete().where(self.product_entity.c.id == id)
        result = self.conn.execute(query)
        self.conn.commit()

        return result.rowcount
