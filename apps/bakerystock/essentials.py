from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from bson.objectid import ObjectId

dburi = 'postgresql://pgusr:pgusr@bakerystockdb.inmar-net/bakerystockdb'


def fetch_data(sql, dburi=dburi):
    cnx = connect(dburi)
    with cnx.cursor(cursor_factory=RealDictCursor) as dbcur:
        dbcur.execute(sql)
        sql_dat = dbcur.fetchall()
    cnx.close()

    return sql_dat


def execute_sql(sql, dburi=dburi):
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
