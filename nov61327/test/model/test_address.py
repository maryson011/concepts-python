import unittest

from src.model.address import Address

class TestAddress(unittest.TestCase):
    def setUp(self):
        self.address = Address('MZ-0-002-000-00')
        self.a2 = Address('MZ-0-002-000-00')

    def test_get_address_str(self):
        self.assertEqual(str(self.address), 'address: MZ-0-002-000-00')

    def test_eq_address(self):
        self.assertEqual(self.address, self.a2)