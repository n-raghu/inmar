from essentials import fetch_data


def fetch_sku(**kwargs):
    page = kwargs.pop('page')
    where_clause = ''
    for k,v in kwargs.items():
        if v:
            where_clause += f"{k}='{v}' AND "
    where_clause = f'WHERE {where_clause[:-5]}' if where_clause else ''

    qry = f'''
            SELECT
                *
            FROM
                sku
            {where_clause if where_clause else ''}
    '''

    return fetch_data(page, qry)
