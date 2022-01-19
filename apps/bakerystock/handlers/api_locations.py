import traceback
from fastapi import APIRouter

from resources.locations import fetch_locations

api = APIRouter()


@api.get('/locations')
def all_locations():

    try:
        return fetch_locations()
    except Exception as err:
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
