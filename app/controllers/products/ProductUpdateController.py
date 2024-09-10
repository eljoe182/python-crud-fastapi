from context.products.application import ProductUpdateUseCase
from context.products.domain.schemas.ProductSchema import ProductUpdateSchema


class ProductUpdateController:
    def __init__(self, use_case: ProductUpdateUseCase):
        self._use_case = use_case

    def run(self, id: int, product: ProductUpdateSchema):
        return self._use_case.execute(id, product)
