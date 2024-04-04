import requests


def get_book_by_params(firstname="", lastname=""):
    return requests.get(f'https://restful-booker.herokuapp.com/booking/?firstname={firstname}&lastname={lastname}')


def get_booking(id_book):
    return requests.get(f"https://restful-booker.herokuapp.com/booking/{id_book}")


def get_all_books_id():
    return requests.get(f"https://restful-booker.herokuapp.com/booking/")


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
    return requests.post(f"https://restful-booker.herokuapp.com/booking", json=body)

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
    return requests.post(f"https://restful-booker.herokuapp.com/booking", json=body)
