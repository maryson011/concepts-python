import os, sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.model.address import Address
from src.model.product import Product


class Checkin:
    def __init__(self, address: Address, product: Product):
        if not isinstance(address, Address):
            raise TypeError('Address invalid')
        if not isinstance(product, Product):
            raise TypeError('Product invalid')    
        self.address = address
        self.product = product

    def get_movement(self):
        return f'{self.address.get_address()} + {self.product.get_product()}'
    
# if __name__ == '__main__':
#     p1 = Product('DDDD12345', 'Book', 'description book')
#     a1 = Address('MZ-0-002-000-00')
# 
#     c1 = Checkin(a1, p1)
#     print(c1.get_movement())