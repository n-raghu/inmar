import logging
import traceback
from fastapi import APIRouter, Response

from resources import locations
from schemamodels import SchemaPostLocations

logging.basicConfig(level=logging.INFO)
api = APIRouter()

point_location = '/location'


@api.get(point_location)
def all_locations(response: Response):
    try:
        return locations.fetch_locations()
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
        locations.create_locations(input_dict)
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
