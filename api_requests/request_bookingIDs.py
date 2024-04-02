import requests


def get_GetBookingIds(firstname="", lastnane="", checkin="", checkout=""):
    return requests.get(
        f"https://restful-booker.herokuapp.com/booking/firstname=%7Bfirstname%7D&lastname=%7Blastnane%7D&checkin=%7Bcheckin%7D&checkout=%7Bcheckout%7D")


def get_booking(Id_book):
    return requests.get(f"https://restful-booker.herokuapp.com/booking/%7BId_book%7D")

def get_all_books_id():
    return requests.get(f"https://restful-booker.herokuapp.com/booking/")