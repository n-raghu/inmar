import logging
import traceback
from fastapi import APIRouter, Response

from resources import locations
from essentials import record_error
from schemamodels import SchemaPostLocations

logging.basicConfig(level=logging.INFO)
api = APIRouter()

point_location = '/location'
point_desc = 'Location API'


@api.get(point_location)
def all_locations(response: Response, page: int=1):
    try:
        dat_tuple = locations.fetch_locations(page=page)
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
        exc_msg = str(traceback.format_exc())
        response.status_code = 422
        logging.error(exc_msg)
        record_error(
            point_desc,
            err_resource='POST',
            err_msg=exc_msg
        )
        return {
            'request': False,
            'err': err,
            'info': exc_msg
        }
