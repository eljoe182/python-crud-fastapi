from domain.infrastructure.schemas.ProductSchema import ProductStoreSchema
from domain.infrastructure.repositories.ProductRepository import ProductRepository


class ProductStoreUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product: ProductStoreSchema):
        return self.repository.store(product)
