from ..domain.schemas.ProductSchema import ProductUpdateSchema
from ..infrastructure.repositories.ProductRepository import ProductRepository


class ProductUpdateUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, id: int, product: ProductUpdateSchema):
        return self.repository.update(id, product)
