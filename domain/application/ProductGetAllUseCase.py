from ..infrastructure.repositories.ProductRepository import ProductRepository


class ProductGetAllUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()
