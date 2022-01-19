import traceback
from fastapi import APIRouter

api = APIRouter()


@api.get('/')
def loc_about():

    try:
        return {'client': 'inmar'}
    except Exception as err:
        return {
            'request': False,
            'err': err,
            'info': traceback.format_exc()
        }
