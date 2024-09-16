from context.products.application.ProductDeleteUseCase import ProductDeleteUseCase
from unittest.mock import MagicMock


def test_product_delete_use_case():
    data_expected = True
    repository = MagicMock()
    repository.delete.return_value = data_expected

    use_case = ProductDeleteUseCase(repository)
    result = use_case.execute(1)

    assert result == data_expected
