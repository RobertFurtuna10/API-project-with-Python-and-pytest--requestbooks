import requests


def get_token():
    body = {
        "username": "admin",
        "password": "password123"
      }
    response = requests.post("https://restful-booker.herokuapp.com/auth", json=body)
    return response.json()["token"]

print(get_token())