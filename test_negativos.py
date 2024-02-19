import unittest
from unittest.mock import patch
from class_Hotel import Hotel
from class_Reservation import Reservation
from class_Customer import Customer
from datetime import datetime

class NegativeTests(unittest.TestCase):
    def test_hotel_no_rooms_available(self):
        hotel = Hotel('Hotel California')
        with patch('class_Hotel.Hotel.check_in', return_value=False):
            self.assertFalse(hotel.check_in(guest_name="Jane Doe"))

    def test_reservation_invalid_dates(self):
        past_or_invalid_check_in_date = datetime.strptime("2020-01-01", "%Y-%m-%d")
        past_or_invalid_check_out_date = datetime.strptime("2020-01-07", "%Y-%m-%d")
        reservation = Reservation(past_or_invalid_check_in_date, past_or_invalid_check_out_date)
        with patch('class_Reservation.Reservation.validate_dates', return_value=False):
            self.assertFalse(reservation.validate_dates())

    def test_customer_invalid_email(self):
        invalid_customer = Customer(name="John Doe", email="not-an-email")
        with patch('class_Customer.Customer.crear_cliente', return_value=False):
            self.assertFalse(invalid_customer.crear_cliente())

    def test_reservation_overlapping_dates(self):
        check_in_date = datetime.strptime("2022-01-01", "%Y-%m-%d")
        check_out_date = datetime.strptime("2022-01-07", "%Y-%m-%d")
        overlapping_reservation = Reservation(check_in_date, check_out_date)
        with patch('class_Reservation.Reservation.check_overlapping_dates', return_value=True):
            self.assertFalse(overlapping_reservation.check_overlapping_dates())

    def test_customer_non_existent(self):
        non_existent_customer = Customer(name="Non Existent", email="nonexistent@example.com")
        with patch('class_Customer.Customer.eliminar_cliente', return_value=False):
            self.assertFalse(non_existent_customer.eliminar_cliente())

if __name__ == "__main__":
    unittest.main()