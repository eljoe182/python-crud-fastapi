from context.products.application import ProductUpdateUseCase
from context.products.domain.schemas.ProductSchema import ProductStoreSchema


class ProductStoreController:
    def __init__(self, use_case: ProductUpdateUseCase):
        self._use_case = use_case

    def run(self, product: ProductStoreSchema):
        return self._use_case.execute(product)
