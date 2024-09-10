from context.products.infrastructure.repositories.ProductRepository import (
    ProductRepository,
)
from context.products.domain.schemas.ProductSchema import ProductStoreSchema
from unittest.mock import MagicMock


def test_product_repository_get_all():
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
    client = MagicMock()
    client.get_engine().connect().execute().mappings().all.return_value = data_expected

    repository = ProductRepository(client)
    result = repository.get_all()

    assert result == data_expected


def test_product_repository_store():
    data_expected = {
        "id": 1,
        "name": "Product 1",
        "description": "Description 1",
        "price": 1000,
        "is_active": True,
    }
    client = MagicMock()
    client.get_engine().connect().execute().lastrowid = 1
    client.get_engine().connect().execute().mappings().first.return_value = (
        data_expected
    )

    repository = ProductRepository(client)

    new_product = ProductStoreSchema(
        name="Product 1", description="Description 1", price=1000, is_active=True
    )

    result = repository.store(new_product)

    assert result == data_expected


def test_product_repository_get_by_id():
    data_expected = {
        "id": 1,
        "name": "Product 1",
        "description": "Description 1",
        "price": 1000,
        "is_active": True,
    }
    client = MagicMock()
    client.get_engine().connect().execute().mappings().first.return_value = (
        data_expected
    )

    repository = ProductRepository(client)
    result = repository.get_by_id(1)

    assert result == data_expected


def test_product_repository_update():
    data_expected = {
        "id": 1,
        "name": "Product 1",
        "description": "Description 1",
        "price": 1000,
        "is_active": True,
    }
    client = MagicMock()
    client.get_engine().connect().execute().mappings().first.return_value = (
        data_expected
    )

    repository = ProductRepository(client)

    update_product = ProductStoreSchema(
        name="Product 1", description="Description 1", price=1000, is_active=True
    )

    result = repository.update(1, update_product)

    assert result == data_expected


def test_product_repository_delete():
    client = MagicMock()
    client.get_engine().connect().execute().rowcount = 1

    repository = ProductRepository(client)
    result = repository.delete(1)

    assert result == 1
