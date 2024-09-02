from .app import app
from .routes.ProductRoutes import router as product_router

app.include_router(product_router)
