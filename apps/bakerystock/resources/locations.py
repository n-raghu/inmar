import logging

from essentials import fetch_data, execute_sql


def fetch_locations(**kwargs):
    qry = '''
            SELECT
                *
            FROM
                location
    '''
    where_clause = ''
    for k,v in kwargs.items():
        where_clause += f"{k}='{v}' AND "
    if where_clause:
        qry = qry + ' WHERE ' + where_clause[:-5]
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
