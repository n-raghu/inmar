from asyncio import as_completed
import sys
import glob
import logging
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed

from psycopg2 import connect


def fetch_csv_headers(csvfile):
    with open(csvfile, 'r') as csv_obj:
        for row in csv_obj:
            return row.lower()


def fetch_files(path):
    return glob.iglob(f'{path}/*.csv', recursive=True)


def csv_to_tbl(csvfile, dburi):
    cnx = connect(dburi)
    tbl_header = fetch_csv_headers(csvfile)
    file_name = csvfile.split('/')[-1]
    tbl = file_name.split('.')[0]
    csv_sep = ','
    null_pattern = 'NULL'

    pg_cp_statement = f"COPY {tbl}({tbl_header}) FROM STDIN WITH DELIMITER '{csv_sep}' CSV HEADER NULL '{null_pattern}' "

    with cnx.cursor() as dbcur:
        with open(csvfile, 'r') as csv_obj:
            dbcur.copy_expert(sql=pg_cp_statement, file=csv_obj)
        cnx.commit()
    cnx.close()

    return f"Finished - {tbl}"


def aio_ingester(files, dburi):
    with ProcessPoolExecutor(max_workers=5) as executor:
        pool_dict = {
            executor.submit(
                csv_to_tbl,
                file_,
                dburi
            ): file_ for file_ in files
        }
    
    for futur_ in as_completed(pool_dict):
        print(futur_.result())


if __name__ == '__main__':
    try:
        logging.info("CHECKING FOR FILES")
        dat_file_path = '../dat'
        dburi = 'postgresql://pgusr:pgusr@bakerystockdb.inmar-net/bakerystockdb'
        files = fetch_files(dat_file_path)
        aio_ingester(files, dburi)
    except Exception:
        logging.error(str(traceback.format_exc()))
        sys.exit()
