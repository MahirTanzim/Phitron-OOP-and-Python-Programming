class Animal:
    def __init__(self, name):
        self.name = name


    def make_sound(self):
        print("Makeing Sound")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print("Mew mew")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Gheo Gheo")


dogie1 = Dog("Rifat")

dogie2 = Dog("Dogie")

biloi = Cat("Biloi")



animals = [dogie1, dogie2, biloi]


for animal in animals:
    animal.make_sound()
