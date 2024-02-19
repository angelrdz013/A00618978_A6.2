import unittest
from class_Customer import Customer
import os

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer('Test Customer', 'testcustomer@example.com')
        self.filename = 'clientes_test.json'
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_crear_cliente(self):
    
    def test_eliminar_cliente(self):
       
    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()