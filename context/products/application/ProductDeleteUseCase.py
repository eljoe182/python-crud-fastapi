from ..infrastructure.repositories import ProductRepository


class ProductDeleteUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, id: int):
        return self.repository.delete(id)
