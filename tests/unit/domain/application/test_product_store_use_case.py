from context.products.application.ProductStoreUseCase import ProductStoreUseCase
from unittest.mock import MagicMock


def test_product_store_use_case():
    data_expected = {
        "id": 1,
        "name": "Product 1",
        "description": "Description 1",
        "price": 1000,
        "is_active": True,
    }
    repository = MagicMock()
    repository.store.return_value = data_expected

    use_case = ProductStoreUseCase(repository)
    result = use_case.execute(data_expected)

    assert result == data_expected
