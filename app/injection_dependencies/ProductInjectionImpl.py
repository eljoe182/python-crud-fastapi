from app.controllers.products import (
    ProductGetAllController,
    ProductDeleteController,
    ProductFindByIdController,
    ProductStoreController,
    ProductUpdateController,
)
from context.products.application import (
    ProductDeleteUseCase,
    ProductFindByIdUseCase,
    ProductGetAllUseCase,
    ProductStoreUseCase,
    ProductUpdateUseCase,
)
from context.products.infrastructure.repositories.ProductRepository import (
    ProductRepository,
)
from shared.infrastructure.persistence.mysql import MySQLClient, MySQLConfig


class ProductInjectionImpl:
    def product_get_all_impl():
        mysql_client = MySQLClient(MySQLConfig())
        product_repository = ProductRepository(mysql_client)
        use_case = ProductGetAllUseCase(product_repository)
        return ProductGetAllController(use_case)

    def product_store_impl():
        mysql_client = MySQLClient(MySQLConfig())
        product_repository = ProductRepository(mysql_client)
        use_case = ProductStoreUseCase(product_repository)
        return ProductStoreController(use_case)

    def product_find_by_id_impl():
        mysql_client = MySQLClient(MySQLConfig())
        product_repository = ProductRepository(mysql_client)
        use_case = ProductFindByIdUseCase(product_repository)
        return ProductFindByIdController(use_case)

    def product_update_impl():
        mysql_client = MySQLClient(MySQLConfig())
        product_repository = ProductRepository(mysql_client)
        use_case = ProductUpdateUseCase(product_repository)
        return ProductUpdateController(use_case)

    def product_delete_impl():
        mysql_client = MySQLClient(MySQLConfig())
        product_repository = ProductRepository(mysql_client)
        use_case = ProductDeleteUseCase(product_repository)
        return ProductDeleteController(use_case)
