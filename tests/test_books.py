from api_requests import request_books


class TestBooks:

    def test_get_booking_by_id(self):
        response = request_books.get_booking(3)
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        assert "firstname" in response.json()
        assert "lastname" in response.json()
        assert "checkin" in response.json()["bookingdates"]
        assert "checkout" in response.json()["bookingdates"]

    def test_get_all_books_id(self):
        response = request_books.get_all_books_id()
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        assert len(response.json()) > 0
        for element in response.json():
            assert "bookingid" in element
            # print(element)

    def test_get_book_id_by_firstname(self):
        response = request_books.get_book_by_params("Mark")
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        for element in response.json():
            assert "bookingid" in element
            # print(element)

    def test_create_book_positive_tes(self):
        response = request_books.create_book("Adrian", "Storm", 132, True, "2018-01-01", "2019-01-01", "Breakfast")
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        assert "bookingid" in response.json()
        assert response.json()['booking']['firstname'] == 'Adrian'
        # print(response.json()['booking']['firstname']) //for verification
        assert response.json()['booking']['bookingdates']['checkin'] == "2018-01-01"
        assert response.json()['booking']['bookingdates']['checkout'] == '2019-01-01'
        assert response.json()['booking']['lastname'] == 'Storm'
        assert response.json()['booking']['totalprice'] == 132
        assert response.json()['booking']['depositpaid'] == True
        assert response.json()['booking']['additionalneeds'] == "Breakfast"

    def test_create_book_without_introducing_firstname(self):
        response = request_books.create_book_without_firstname("Storm", 132, True, "2018-01-01", "2019-01-01",
                                                               "Breakfast")
        assert response.status_code == 500, f"Actual: {response.status_code}, Expected: 500"

    def test_create_book_with_string_value_for_total_price(self):
        response = request_books.create_book("Adrian", "Storm", '132', True, "2018-01-01", "2019-01-01",
                                             "Breakfast")
        assert response.status_code != 200, (
            f"Actual: {response.status_code}. The request was expected to fail because "
            "a string value was provided for the total price, which is required to be an "
            "integer according to the documentation.")

