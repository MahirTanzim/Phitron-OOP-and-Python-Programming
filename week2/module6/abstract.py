from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def eat(self):
        print("kola khao")

    def move(self):
        pass



class Monkey(Animal):
    def __init__(self, name):
        self.catagory = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        print("Damn Tha Banana is good")


lucky = Monkey("Lucky")

print(lucky.catagory)
lucky.eat()