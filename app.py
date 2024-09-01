from fastapi import FastAPI
from routes.ProductRoutes import router as product_router

app = FastAPI()

app.include_router(product_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
