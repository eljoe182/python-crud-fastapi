from context.products.application.ProductGetAllUseCase import ProductGetAllUseCase
from unittest.mock import MagicMock
from shared.Errors import UseCaseError


def test_product_get_all_use_case():
    data_expected = [
        {
            "id": 1,
            "name": "Product 1",
            "description": "Description 1",
            "price": 1000,
            "is_active": True,
        },
        {
            "id": 2,
            "name": "Product 2",
            "description": "Description 2",
            "price": 2000,
            "is_active": False,
        },
    ]
    repository = MagicMock()
    repository.get_all.return_value = data_expected

    use_case = ProductGetAllUseCase(repository)
    result = use_case.execute()

    assert result == data_expected


def test_product_get_all_use_case_empty():
    data_expected = []
    repository = MagicMock()
    repository.get_all.return_value = data_expected

    use_case = ProductGetAllUseCase(repository)
    result = use_case.execute()

    assert result == data_expected


def test_product_get_all_use_case_none():
    data_expected = None
    repository = MagicMock()
    repository.get_all.return_value = data_expected

    use_case = ProductGetAllUseCase(repository)
    result = use_case.execute()

    assert result == data_expected


def test_product_get_all_use_case_error():
    data_expected = UseCaseError("Error ProductGetAllUseCase")
    repository = MagicMock()
    repository.get_all.side_effect = data_expected

    use_case = ProductGetAllUseCase(repository)
    result = use_case.execute()

    assert result == data_expected
