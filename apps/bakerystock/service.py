from fastapi import FastAPI
from handlers.api_locations import api as api_locations
from handlers.api_sku import api as api_sku

app = FastAPI()
app.include_router(api_sku)
app.include_router(api_locations)
