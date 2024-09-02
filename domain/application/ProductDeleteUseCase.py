from domain.infrastructure.repositories.ProductRepository import ProductRepository


class ProductDeleteUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def delete(self, id: int):
        self.repository.delete(id)
