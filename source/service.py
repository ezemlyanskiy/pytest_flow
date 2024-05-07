from http import HTTPStatus

import requests

ENDPOINT = 'https://jsonplaceholder.typicode.com/users'


database = {
    1: 'Alice',
    2: 'Bob',
    3: 'Charlie',
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_users():
    response = requests.get(ENDPOINT)
    if response.status_code == HTTPStatus.OK:
        return response.json()
    raise requests.HTTPError
