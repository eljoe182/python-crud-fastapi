from shared.models.BaseController import BaseController
from context.products.application import ProductDeleteUseCase


class ProductDeleteController(BaseController):
    def __init__(self, use_case: ProductDeleteUseCase):
        self._use_case = use_case

    def run(self, id: int):
        return self._use_case.execute(id)
