from domain.infrastructure.schemas.ProductSchema import ProductUpdateSchema
from domain.infrastructure.repositories.ProductRepository import ProductRepository


class ProductUpdateUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, id: int, product: ProductUpdateSchema):
        self.repository.update(id, product)
