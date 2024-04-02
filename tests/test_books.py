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
            print(element)
