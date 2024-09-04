from ..infrastructure.repositories.ProductRepository import ProductRepository
from domain.infrastructure.shared.Errors import UseCaseError
from domain.infrastructure.shared.Logging import Logging


class ProductGetAllUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        try:
            return self.repository.get_all()
        except UseCaseError as error:
            Logging.error(error)
            return error
