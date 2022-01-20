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
    logging.info(qry)
    return fetch_data(qry)


def create_locations(dict_location: dict):
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


def update_locations(dict_location: dict):
    set_params = ''
    for k,v in dict_location.items():
        set_params += f"{k}='{v}', "
    qry = f'''
            UPDATE
                    location
            SET
                    {set_params.strip()[:-1]}
    '''
    logging.info(qry)
    execute_sql(qry)


def del_locations(dict_location: dict):
    qry = f'''

    '''
    logging.info(qry)
    execute_sql(qry)


if __name__ == '__main__':
    print(fetch_locations())
