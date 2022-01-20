from fastapi import FastAPI
from handlers.api_sku import api as api_sku
from handlers.api_location import api as api_location
from handlers.api_location_xtn import api as api_location_xtn

app = FastAPI(
    title="BakeryStock APIs",
    description='APIs to interact with BakeryStock and Inventory',
    docs_url='/bakerystock',
    version='0.1',
)

app.include_router(api_sku, prefix='/api/v1')
app.include_router(api_location, prefix='/api/v1')
app.include_router(api_location_xtn, prefix='/api/v1')
