from shared.models.BaseUseCase import BaseUseCase
from ..infrastructure.repositories.ProductRepository import ProductRepository


class ProductFindByIdUseCase(BaseUseCase):
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, id: int):
        return self.repository.get_by_id(id)
