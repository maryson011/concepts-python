import re

class Address:

    __REGEX = '^[A-Z]{2}-\\d-\\d{3}-\\d{3}-\\d{2}$'

    def __init__(self, address):
        valido = self.isValido(address)
        if valido:
            self.__address = address

    def get_address(self):
        return self.__address
    
    def __str__(self) -> str:
        return f'address: {self.__address}'
    
    def __eq__(self, value) -> bool:
        return self.__address == value.__address

    def isValido(self, address):
        return bool(re.match(self.__REGEX, address))

# a1 = Address('MZ-0-001-000-00')
# print(a1)

