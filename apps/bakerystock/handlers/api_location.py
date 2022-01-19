import logging
import traceback
from fastapi import APIRouter, Response

from schemamodels import SchemaPostLocations
from resources.locations import fetch_locations, post_locations

logging.basicConfig(level=logging.INFO)
api = APIRouter()

point_location = '/location'
point_category = '/location/{location_id}/department/{department_id}/category/{category_id}/subcategory/{subcategory_id}'


@api.get(point_location)
def all_locations(response: Response):
    try:
        return fetch_locations()
    except Exception as err:
        response.status_code = 422
        return {
            'request': False,
            'err': err,
            'info': traceback.format_exc()
        }


@api.post(point_location)
def post_location(body: SchemaPostLocations, response: Response):
    try:
        input_dict = body.dict()
        logging.info(input_dict)
        post_locations(input_dict)
        response.status_code = 201
        input_dict['request'] = True
        return input_dict

    except Exception as err:
        response.status_code = 422
        return {
            'request': False,
            'err': err,
            'info': traceback.format_exc()
        }


@api.get(point_category)
def get_category(
    response: Response,
    location_id: str,
    department_id: str,
    category_id: str,
    subcategory_id: str
):
    try:
        return fetch_locations(
            location=location_id,
            department=department_id,
            category=category_id,
            subcategory=subcategory_id,
        )
    except Exception as err:
        response.status_code = 422
        logging.error(str(traceback.format_exc()))
        return {
            'request': False,
            'err': err,
            'info': traceback.format_exc()
        }
