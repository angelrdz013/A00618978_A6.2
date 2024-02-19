import unittest
from class_Hotel import Hotel
import os

class TestHotel(unittest.TestCase):

    def setUp(self):
        """Preparar condiciones para las pruebas."""
        self.hotel = Hotel('Test Hotel', 'Test Location', 100)
        self.filename = 'hoteles_test.json'
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_crear_hotel(self):
        """Test para la creación de un hotel nuevos.""
    
    def test_eliminar_hotel(self):
        """Test para eliminar un hotel existente.""
    
    def tearDown(self):
        """Limpiar después de cada método de prueba."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()