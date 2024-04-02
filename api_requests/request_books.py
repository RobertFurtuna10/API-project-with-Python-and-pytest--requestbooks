import requests


def get_book_by_params(firstname="", lastname=""):
    return requests.get(f'https://restful-booker.herokuapp.com/booking/?firstname={firstname}&lastname={lastname}')


def get_booking(id_book):
    return requests.get(f"https://restful-booker.herokuapp.com/booking/{id_book}")


def get_all_books_id():
    return requests.get(f"https://restful-booker.herokuapp.com/booking/")
