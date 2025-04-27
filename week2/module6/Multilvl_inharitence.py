class vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def run(self):
        print(f"{self.name} is running")

    def __repr__(self):
        return f"Name: {self.name}, Price: {self.price}"



class Bus(vehicle):
    def __init__(self, name, price, capacity):
        super().__init__(name, price)
        self.capacity = capacity
            
    # def run(self):
    #     print(f"{self.name} is running with a capacity of {self.capacity} passengers")
    
    def __repr__(self):
        return super().__repr__() + f", Capacity: {self.capacity}"


class Truck(vehicle):
    def __init__ (self, name, price, load_capaciry):
        super().__init__(name,price)
        self.load_capaciry = load_capaciry


class PicUpTruck(Truck):
    def __init__(self, name, price, load_capaciry, weight):
        self.weight = weight
        super().__init__(name, price, load_capaciry)


class ACBus(Bus):
    def __init__(self, name, price, capacity, sleeper):
        super().__init__(name, price, capacity)
        self.sleeper = sleeper
    
    def __repr__(self):
        return super().__repr__() + f", Sleeper: {self.sleeper}"



greenline = ACBus("GreenLine", 50000000, 25, True)

greenline.run()
print(greenline)

print(ACBus.__mro__)
