import logging
import traceback
from fastapi import APIRouter, Response

from schemamodels import SchemaPostLocations
from resources.locations import fetch_locations, post_locations

logging.basicConfig(level=logging.INFO)
api = APIRouter()


@api.get('/locations')
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


@api.post('/locations')
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


@api.get('/location/{location_id}/department')
def location_depts():

    try:
        return fetch_locations()
    except Exception as err:
        return {
            'request': False,
            'err': err,
            'info': traceback.format_exc()
        }
