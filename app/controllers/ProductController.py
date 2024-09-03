from domain.application import (
    ProductDeleteUseCase,
    ProductFindByIdUseCase,
    ProductGetAllUseCase,
    ProductStoreUseCase,
    ProductUpdateUseCase,
)
from domain.infrastructure.repositories.ProductRepository import ProductRepository
from domain.infrastructure.persistence.mysql import MySQLClient, MySQLConfig
from domain.infrastructure.schemas.ProductSchema import (
    ProductStoreSchema,
    ProductUpdateSchema,
)


class ProductController:
    def __init__(self):
        self.repository = ProductRepository(MySQLClient(MySQLConfig()))

    def get_all_products(self):
        use_case = ProductGetAllUseCase(self.repository)
        return use_case.execute()

    def store_product(self, product: ProductStoreSchema):
        use_case = ProductStoreUseCase(self.repository)
        return use_case.execute(product)

    def get_by_id_product(self, id: int):
        use_case = ProductFindByIdUseCase(self.repository)
        return use_case.execute(id)

    def update_product(self, id: int, product: ProductUpdateSchema):
        use_case = ProductUpdateUseCase(self.repository)
        return use_case.execute(id, product)

    def delete_product(self, id: int):
        use_case = ProductDeleteUseCase(self.repository)
        return use_case.execute(id)
