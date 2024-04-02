from api_requests import request_bookingIDs

class TestBooks:

    def test_get_booking(self):
        response = request_bookingIDs.get_booking(5)
        assert response.status_code == 200, f"Actual: {response.status_code}, Expected: 200"
        assert "firstname" in response.json()
        assert "lastname" in response.json()
        assert "checkin" in response.json()["bookingdates"]
        assert "checkout" in response.json()["bookingdates"]

    def test_get_books_id(self):
        response = request_bookingIDs.get_all_books_id()
        assert response.status_code == 200 , f"Actual: {response.status_code}, Expected: 200"
        assert len(response.json()) > 0
        for element in response.json():
            assert "bookingid" in element
            print()
        # assert "bookingid" in response.json()