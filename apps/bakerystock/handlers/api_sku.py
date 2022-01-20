import logging
import traceback
from fastapi import APIRouter, Response

from essentials import record_error
from resources.sku import fetch_sku

api = APIRouter()
point_sku = '/sku'
point_desc = 'SKU API'


@api.get(point_sku)
def get_sku(
    response: Response,
    location: str=None,
    department: str=None,
    category: str=None,
    subcategory: str=None,
    page: int=1,
):
    try:
        dat_tuple = fetch_sku(
            page=page,
            location=location,
            department=department,
            category=category,
            subcategory=subcategory
        )
        dat_ = dat_tuple[0]
        response.headers["Total-Records"] = str(dat_tuple[1])
        response.headers["Total-Pages"] = str(dat_tuple[2])
        response.headers["Page-Rows"] = str(len(dat_))
        return dat_
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