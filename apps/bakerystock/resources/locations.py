from essentials import fetch_data


def fetch_locations():
    qry = '''
            SELECT
                *
            FROM
                location
    '''
    return fetch_data(qry)


if __name__ == '__main__':
    print(fetch_locations())
