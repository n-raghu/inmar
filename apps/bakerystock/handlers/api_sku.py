import traceback
from fastapi import APIRouter, Response

from resources.sku import fetch_sku

api = APIRouter()


@api.get('/sku')
def all_locations(
    response: Response,
    location: str=None,
    department: str=None,
    category: str=None,
    subcategory: str=None,
):
    try:
        return fetch_sku(
            location=location,
            department=department,
            category=category,
            subcategory=subcategory
        )
    except Exception as err:
        response.status_code = 422
        return {
            'request': False,
            'err': err,
            'info': traceback.format_exc()
        }
