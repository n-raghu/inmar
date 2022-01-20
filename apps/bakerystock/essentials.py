import math
import yaml
import logging
from psycopg2 import connect
from bson.objectid import ObjectId
from psycopg2.extras import RealDictCursor

with open('env.yml') as yfile:
    CFG = yaml.safe_load(yfile.read())


def fetch_data(page, sql, cfg=CFG):
    datastore_cfg=CFG['datastore']
    dburi = f"{datastore_cfg['engine']}://{datastore_cfg['uid']}:{datastore_cfg['pwd']}@{datastore_cfg['host']}/{datastore_cfg['dbname']}"
    api_page_size = cfg['api_standard_page_size']
    cnx = connect(dburi)
    qry = f'{sql} OFFSET {(page - 1) * api_page_size}'
    logging.info(f'Final Query - {qry}')
    with cnx.cursor(cursor_factory=RealDictCursor) as dbcur:
        dbcur.execute(qry)
        nrows = dbcur.rowcount
        next_pages = math.ceil(nrows/api_page_size)
        sql_dat = dbcur.fetchmany(api_page_size)
    cnx.close()

    return sql_dat, nrows + (api_page_size * (page-1)), next_pages + page - 1


def execute_sql(sql, datastore_cfg=CFG['datastore']):
    dburi = f"{datastore_cfg['engine']}://{datastore_cfg['uid']}:{datastore_cfg['pwd']}@{datastore_cfg['host']}/{datastore_cfg['dbname']}"
    cnx = connect(dburi)
    with cnx.cursor() as dbcur:
        dbcur.execute(sql)
    cnx.commit()
    cnx.close()


def record_error(err_class, err_resource, err_msg):
    oid = str(ObjectId())
    qry = f'''
            INSERT INTO
                    errorlogs(tbl_id, err_class, err_resource, err_msg)
            SELECT
                    '{oid}', '{err_class}', '{err_resource}', '{err_msg}'
    '''
    execute_sql(qry)
