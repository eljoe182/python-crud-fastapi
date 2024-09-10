from .app import app
from .routes.ProductRoutes import router as product_router

def database_init():
    from shared.infrastructure.persistence.mysql import MySQLClient, MySQLConfig
    from context.products.infrastructure.repositories.entities.ProductEntity import ProductEntity

    mysql_config = MySQLConfig()
    mysql_client = MySQLClient(mysql_config)
    product_entity = ProductEntity(mysql_client)
    product_entity.create_table()

database_init()

app.include_router(product_router)
