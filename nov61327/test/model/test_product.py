import unittest

from src.model.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product('DDDD12345', 'Book', 'description book')
        self.sku = self.product.get_sku()

    def test_product_sku(self):
        self.assertEqual(self.product.get_sku(), self.sku)