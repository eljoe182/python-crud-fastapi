from shared.Errors import UseCaseError
from shared.Logging import Logging
from ..infrastructure.repositories.ProductRepository import ProductRepository


class ProductGetAllUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        try:
            return self.repository.get_all()
        except UseCaseError as error:
            Logging.error(error)
            return error
