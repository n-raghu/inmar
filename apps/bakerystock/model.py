import sqlalchemy as say
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()

DT = say.Date
TXT = say.Text
COL = say.Column
STR = say.String
FLOAT = say.Float
NUM = say.NUMERIC
INT = say.Integer
TABLE = say.Table
BOOL = say.Boolean
BIGINT = say.BIGINT
LBY = say.LargeBinary
TIMES = say.TIMESTAMP


class Location(BASE):
    __tablename__ = 'location'
    active = COL(BOOL, server_default=True)
    location = COL(TXT)
    department = COL(TXT)
    category = COL(TXT)
    subcategory = COL(TXT)
    location_id = COL(INT, autoincrement=True, primary_key=True)
    db_stamp = COL(TIMES, server_default=say.sql.text('CURRENT_TIMESTAMP'))


class ErrorLogs(BASE):
    __tablename__ = 'errorlogs'
    err_class = COL(STR)
    err_resource = COL(STR)
    err_msg = COL(STR)
    app_stamp = COL(TIMES)
    db_stamp = COL(TIMES, server_default=say.sql.text('CURRENT_TIMESTAMP'))
    tbl_id = COL(TXT, primary_key=True)


class SKU(BASE):
    __tablename__ = 'sku'
    sku = COL(INT, primary_key=True)
    name = COL(TXT)
    location = COL(TXT)
    department = COL(TXT)
    category = COL(TXT)
    subcategory = COL(TXT)
