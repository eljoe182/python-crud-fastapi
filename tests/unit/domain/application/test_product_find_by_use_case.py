from context.products.application.ProductFindByIdUseCase import ProductFindByIdUseCase
from unittest.mock import MagicMock

def test_product_find_by_use_case():
    data_expected = {
        "id": 1,
        "name": "Product 1",
        "description": "Description 1",
        "price": 1000,
        "is_active": True,
    }
    repository = MagicMock()
    repository.get_by_id.return_value = data_expected

    use_case = ProductFindByIdUseCase(repository)
    result = use_case.execute(1)

    assert result == data_expected