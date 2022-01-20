import logging
import traceback
from fastapi import APIRouter, Response

from essentials import record_error
from resources.sku import fetch_sku

api = APIRouter()
point_sku = '/sku'
point_desc = 'SKU API'


@api.get(point_sku)
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
        exc_msg = str(traceback.format_exc())
        response.status_code = 422
        logging.error(exc_msg)
        record_error(
            point_desc,
            err_resource='GET',
            err_msg=exc_msg
        )
        return {
            'request': False,
            'err': err,
            'info': exc_msg
        }