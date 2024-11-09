import unittest
from src.model.address import Address
from src.model.product import Product
from src.model.actions.checkin import Checkin

class TestCheckin(unittest.TestCase):
    def setUp(self):
        self.product = Product('DDDD12345', 'Book', 'description book')
        self.address = Address('MZ-0-002-000-00')
        self.checkin = Checkin(self.address, self.product)

    def test_initialization(self):
        self.assertIsInstance(self.checkin.address, Address)
        self.assertIsInstance(self.checkin.product, Product)

    def test_get_movement(self):
        expected_movement = f'{self.address.get_address()} + {self.product.get_product()}'
        self.assertEqual(self.checkin.get_movement(), expected_movement)

    def test_invalid_address(self):
        with self.assertRaises(TypeError):
            Checkin("invalid_address", self.product)

    def test_invalid_product(self):
        with self.assertRaises(TypeError):
            Checkin(self.address, "invalid_product")

if __name__ == '__main__':
    unittest.main()
