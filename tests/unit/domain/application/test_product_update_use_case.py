from unittest.mock import MagicMock
from context.products.application.ProductUpdateUseCase import ProductUpdateUseCase


def test_product_update_use_case():
    data_expected = {
        "id": 1,
        "name": "Product 1",
        "description": "Description 1",
        "price": 1000,
        "is_active": True,
    }
    id = 1
    data = {
        "name": "Product 1",
        "description": "Description 1",
        "price": 1000,
        "is_active": True,
    }
    repository = MagicMock()
    repository.update.return_value = data_expected

    use_case = ProductUpdateUseCase(repository)
    result = use_case.execute(id, data)

    assert result == data_expected
    assert repository.update.called
    assert repository.update.call_count == 1
    repository.update.assert_called_with(id, data)
    assert id == result["id"]
