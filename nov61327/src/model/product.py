class Product:
    def __init__(self, sku, name, description):
        self.sku = sku
        self.name = name
        self.description = description

    def get_product(self):
        product = f"{self.sku} - {self.name} - {self.description}"
        return product
    
    def get_sku(self):
        return self.sku

# if __name__ == '__main__':   
#     p1 = Product('SDFE3554', 'Book', 'book description')
#     print(p1.get_product())