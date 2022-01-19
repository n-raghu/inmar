from fastapi import FastAPI
from handlers.api_sku import api as api_sku
from handlers.api_location import api as api_location

app = FastAPI()
app.include_router(api_sku)
app.include_router(api_location)
