import requests
from api_requests import request_token

token = request_token.get_token()

Headers = {
    "Authorization": f"Bearer {token}"
}

url = 'https://restful-booker.herokuapp.com/booking'


def get_book_by_params(firstname="", lastname=""):
    return requests.get(url=url + f'/?firstname={firstname}' + f'&lastname={lastname}')


def get_booking(id_book):
    return requests.get(url=url + '/' + str(id_book))


def get_all_books_id():
    return requests.get(url)


def create_book(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    body = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }
    return requests.post(url=url, json=body)


def create_book_without_firstname(lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    body = {
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }
    return requests.post(url=url, json=body)


def update_book(id_book):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # Send PUT request
    return requests.put(url + '/' + str(id_book), headers=headers, json=payload)


def update_partial_booking_with_token(id_book):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # Send PUT request
    return requests.put(url + '/' + str(id_book), headers=headers, json=payload)


def get_delete_book(id_book):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    # Send Delete request
    return requests.delete(url + '/' + str(id_book), headers=headers)
