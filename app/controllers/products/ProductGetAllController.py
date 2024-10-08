from shared.models.BaseController import BaseController
from context.products.application import ProductGetAllUseCase


class ProductGetAllController(BaseController):
    def __init__(self, use_case: ProductGetAllUseCase):
        self._use_case = use_case

    def run(self):
        return self._use_case.execute()
