class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Vat Mangso, Plao Korma")

    def exercise(self):
        raise NotImplementedError


class cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    
    # override
    def eat(self):
        print("Vegitables")

    def exercise(self):
        print("ksjhbfiowkhrfw")



sakib = cricketer("Sakib", 23, 68, 70, "BD")

# sakib.eat()
# sakib.exercise()

