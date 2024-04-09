from api_requests import request_books
from assertpy import assert_that


class TestBooks:

    def test_get_booking_by_id(self):
        response = request_books.get_booking(3)
        booking_data = response.json()
        assert_that(response.status_code).is_equal_to(200)
        assert_that(booking_data).contains_key("firstname")
        assert_that(booking_data).contains_key("lastname")
        assert_that(booking_data["bookingdates"]).contains_key("checkin")
        assert_that(booking_data["bookingdates"]).contains_key("checkout")

    def test_get_booking_by_using_invalid_id(self):
        response = request_books.get_booking(-33)
        assert_that(response.status_code).is_equal_to(404)

    def test_get_booking_id_by_special_character(self):
        response = request_books.get_booking("=")
        assert_that(response.status_code).is_equal_to(404)

    def test_get_all_books_id(self):
        response = request_books.get_all_books_id()
        assert_that(response.status_code).is_in(200)
        assert_that(len(response.json())).is_greater_than(0)
        for element in response.json():
            assert_that(element).contains_key("bookingid")
            # print(element)

    def test_get_book_id_by_firstname(self):
        response = request_books.get_book_by_params("Mark")
        assert_that(response.status_code).is_equal_to(200)
        for element in response.json():
            assert_that(element).contains_key("bookingid")
            # print(element)

    def test_create_book_with_valid_data(self):
        response = request_books.create_book("Adrian", "Storm", 132, True, "2018-01-01", "2019-01-01", "Breakfast")
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).contains_key("booking")
        assert_that(response.json()['booking']['firstname']).is_equal_to('Adrian')
        assert_that(response.json()['booking']['bookingdates']['checkin']).is_equal_to("2018-01-01")
        assert_that(response.json()['booking']['bookingdates']['checkout']).is_equal_to('2019-01-01')
        assert_that(response.json()['booking']['lastname']).is_equal_to('Storm')
        assert_that(response.json()['booking']['totalprice']).is_equal_to(132)
        assert_that(response.json()['booking']['depositpaid']).is_equal_to(True)
        assert_that(response.json()['booking']['additionalneeds']).is_equal_to("Breakfast")

    def test_create_book_without_introducing_firstname(self):
        response = request_books.create_book_without_firstname("Storm", 132, True, "2018-01-01", "2019-01-01",
                                                               "Breakfast")
        assert_that(response.status_code).is_equal_to(500)

    def test_create_book_with_string_value_for_total_price(self):
        response = request_books.create_book("Adrian", "Storm", '132', True, "2018-01-01", "2019-01-01",
                                             "Breakfast")
        assert_that(response.status_code).is_not_equal_to(200)
        assert_that(response.status_code).is_equal_to(400)
        assert_that(response.json()).does_not_contain_key("booking")

    def test_update_book(self):
        response = request_books.update_book(4)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).contains_key("firstname")
        assert_that(response.json()).contains_key("lastname")
        assert_that(response.json()["bookingdates"]).contains_key("checkin")
        assert_that(response.json()["bookingdates"]).contains_key("checkout")

    def test_update_partial_book_with_token(self):
        response = request_books.update_partial_booking_with_token(3)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).contains_key("firstname")
        assert_that(response.json()).contains_key("lastname")
        assert_that(response.json()["bookingdates"]).contains_key("checkin")
        assert_that(response.json()["bookingdates"]).contains_key("checkout")

    def test_delete_book(self):
        create_book = request_books.create_book("Bobita", "Storm2", 132, True, "2018-02-01", "2019-01-01", "Breakfast")

        id_book_for_delete = create_book.json()['bookingid']

        response = request_books.get_delete_book(id_book_for_delete)

        assert_that(response.status_code).is_equal_to(201)

