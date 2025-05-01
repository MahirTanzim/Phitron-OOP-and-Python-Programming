# read only --> You cant set the value. value cant be shanged
# getter --> get a value of a property through a method. Mostly private property
# setter --> set a value of a property through a method. Mostly private propartu


class User:
    def __init__(self, name, age, money):
        self.name = name
        self._age = age
        self.__money = money

    # getter: Without anu setter is readonly
    @property
    def salary(self):
        return self.__money

    @salary.setter
    def salary(self, value):
        if value < 0:
            return "Can't Be negative"
        else:
            self.__money+=value
samsu = User("Kopa", 23, 12990)
print(samsu.salary)
samsu.salary = 5000
print(samsu.salary)