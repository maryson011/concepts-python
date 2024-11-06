class Animal:
    def __init__(self, nome):
        self.nome = nome

    def expressar(self):
        return "Som do animal..."

class Cachorro(Animal):
    def __init__(self):
        super().__init__("Manteiga")

    def expressar(self):
        return f"{super().expressar()} au au au {self.nome}"

a1 = Cachorro()
print(a1.expressar())