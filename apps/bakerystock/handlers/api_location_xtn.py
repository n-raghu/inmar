import logging
import traceback
from fastapi import APIRouter, Response

from resources import locations
from essentials import record_error
from schemamodels import SchemaPutLocations

api = APIRouter()
point_desc = 'Location Extension API'
logging.basicConfig(level=logging.INFO)
point_category = '/location/{location_id}/department/{department_id}/category/{category_id}/subcategory/{subcategory_id}'

@api.get(point_category)
def get_category(
    response: Response,
    location_id: str,
    department_id: str,
    category_id: str,
    subcategory_id: str,
    page: int=1,
):
    try:
        dat_tuple = locations.fetch_locations(
            page=page,
            location=location_id,
            department=department_id,
            category=category_id,
            subcategory=subcategory_id,
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


@api.put(point_category)
def put_category(
    body: SchemaPutLocations,
    response: Response,
    location_id: str,
    department_id: str,
    category_id: str,
    subcategory_id: str
):
    try:
        input_doc = body.dict()
        locations.update_locations(
            location=location_id,
            department=department_id,
            category=category_id,
            subcategory=subcategory_id,
            input_doc=input_doc
        )
        response.status_code = 204
    except Exception as err:
        exc_msg = str(traceback.format_exc())
        response.status_code = 422
        logging.error(exc_msg)
        record_error(
            point_desc,
            err_resource='PUT',
            err_msg=exc_msg
        )
        return {
            'request': False,
            'err': err,
            'info': exc_msg
        }

@api.delete(point_category)
def del_category(
    response: Response,
    location_id: str,
    department_id: str,
    category_id: str,
    subcategory_id: str
):
    try:
        locations.del_locations(
            location=location_id,
            department=department_id,
            category=category_id,
            subcategory=subcategory_id,
        )
        response.status_code = 204
    except Exception as err:
        exc_msg = str(traceback.format_exc())
        response.status_code = 422
        logging.error(exc_msg)
        record_error(
            point_desc,
            err_resource='DEL',
            err_msg=exc_msg
        )
        return {
            'request': False,
            'err': err,
            'info': exc_msg
        }
