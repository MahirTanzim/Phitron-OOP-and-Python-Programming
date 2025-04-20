class Pen:
    
    def __init__(self, owner, brand, color, attribute, price):
        self.owner = owner
        self.brand = brand
        self.color = color
        self.attribute =attribute
        self.price = price
    
    def write(self, text):
        return f"Write this in the paper: {text}"

mypen = Pen("Mahir", "Matador", "Red", "Ballpoint", 10)
herpen = Pen("Maisha", "Parker", "Blue", "Fountain", 10000)

print(mypen.owner, mypen.brand, mypen. color, mypen.attribute, mypen.price)

print(mypen.write("Joy Bagla"))
