from psycopg2 import connect
from psycopg2.extras import RealDictCursor


dburi = 'postgresql://pgusr:pgusr@bakerystockdb.inmar-net/bakerystockdb'


def fetch_data(sql, dburi=dburi):
    cnx = connect(dburi)
    with cnx.cursor(cursor_factory=RealDictCursor) as dbcur:
        dbcur.execute(sql)
        sql_dat = dbcur.fetchall()
    cnx.close()

    return sql_dat


def execute_sql(sql, dburi=dburi):
    return sql
