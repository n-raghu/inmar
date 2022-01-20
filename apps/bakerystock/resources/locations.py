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


def create_locations(input_doc: dict):
    qry = f'''
            INSERT INTO
                    location(location, department, category, subcategory)
            SELECT
                    '{input_doc.get("location")}',
                    '{input_doc.get("department")}',
                    '{input_doc.get("category")}',
                    '{input_doc.get("subcategory")}';
    '''
    logging.info(qry)
    execute_sql(qry)


def update_locations(
    location: str,
    department: str,
    category: str,
    subcategory: str,
    input_doc: dict
):
    set_params = ''
    for k,v in input_doc.items():
        if v:
            set_params += f"{k}='{v}', "
    qry = f'''
            UPDATE
                    location
            SET
                    {set_params.strip()[:-1]}
            WHERE
                    location='{location}'
            AND     department='{department}' AND category='{category}' AND subcategory='{subcategory}'
    '''
    logging.info(qry)
    execute_sql(qry)


def del_locations(
    location: str,
    department: str,
    category: str,
    subcategory: str,
):
    qry = f'''
            DELETE FROM
                    location
            WHERE
                    location='{location}'
            AND     department='{department}' AND category='{category}' AND subcategory='{subcategory}'
    '''
    logging.info(qry)
    execute_sql(qry)


if __name__ == '__main__':
    print(fetch_locations())
