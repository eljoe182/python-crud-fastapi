from .app import app
from .routes.ProductRoutes import router as product_router
from .routes.AWSRoutes import router as aws_router
from .routes.HealthCheck import router as health_check_router


def database_init():
    from shared.infrastructure.persistence.mysql import MySQLClient, MySQLConfig
    from context.products.infrastructure.repositories.entities.ProductEntity import (
        ProductEntity,
    )

    mysql_config = MySQLConfig()
    mysql_client = MySQLClient(mysql_config)
    product_entity = ProductEntity(mysql_client)
    product_entity.create_table()


database_init()

routes = [aws_router, product_router, health_check_router]
for route in routes:
    app.include_router(route)
