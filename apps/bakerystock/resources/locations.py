import logging

from essentials import fetch_data, execute_sql


def fetch_locations():
    qry = '''
            SELECT
                *
            FROM
                location
    '''
    return fetch_data(qry)


def post_locations(dict_location: dict):
    qry = f'''
            INSERT INTO
                    location(location, department, category, subcategory)
            SELECT
                    '{dict_location.get("location")}',
                    '{dict_location.get("department")}',
                    '{dict_location.get("category")}',
                    '{dict_location.get("subcategory")}';
    '''
    logging.info(qry)
    execute_sql(qry)


if __name__ == '__main__':
    print(fetch_locations())
