import requests

url_aut = 'https://restful-booker.herokuapp.com/auth'


def get_token():
    body = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url_aut, json=body)
    return response.json()["token"]


# print(get_token())
