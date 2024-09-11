from shared.models.BaseUseCase import BaseUseCase
from ..domain.schemas.ProductSchema import ProductStoreSchema
from ..infrastructure.repositories.ProductRepository import ProductRepository


class ProductStoreUseCase(BaseUseCase):
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product: ProductStoreSchema):
        return self.repository.store(product)
