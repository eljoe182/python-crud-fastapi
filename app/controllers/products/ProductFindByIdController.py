from shared.models.BaseController import BaseController
from context.products.application import ProductFindByIdUseCase


class ProductFindByIdController(BaseController):
    def __init__(self, use_case: ProductFindByIdUseCase):
        self._use_case = use_case

    def run(self, id: int):
        return self._use_case.execute(id)
