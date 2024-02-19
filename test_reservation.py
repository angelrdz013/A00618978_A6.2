import unittest
from class_Reservation import Reservation
import os

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.reservation = Reservation('Test Hotel', 'Test Customer', '2023-01-01', '2023-01-05', '101')
        self.filename = 'reservas_test.json'
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_crear_reserva(self):
        # Lógica de prueba
    
    def test_cancelar_reserva(self):
    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()