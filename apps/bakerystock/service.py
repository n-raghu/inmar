from fastapi import FastAPI
from handlers.api_locations import api as api_locations

app = FastAPI()
app.include_router(api_locations)
