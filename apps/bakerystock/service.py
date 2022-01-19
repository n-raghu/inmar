from fastapi import FastAPI
from inmar.apps.bakerystock.handlers.api_location import api as api_location
from handlers.api_sku import api as api_sku

app = FastAPI()
app.include_router(api_sku)
app.include_router(api_location)
