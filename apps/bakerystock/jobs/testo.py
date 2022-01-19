import sys
import glob
import logging
import itertools
import traceback

from psycopg2 import connect

dburi = 'postgresql://pgusr:pgusr@bakerystockdb.inmar-net/bakerystockdb'
cnx = connect(dburi)
tbl = 'location'
tbl_header = 'location,department,category,subcategory'
csv_sep = ','
null_pattern = 'NULL'

pg_cp_statement = f"COPY {tbl}({tbl_header}) FROM STDIN WITH DELIMITER '{csv_sep}' CSV HEADER NULL '{null_pattern}' "
