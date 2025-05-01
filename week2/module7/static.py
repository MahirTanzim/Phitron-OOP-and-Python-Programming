class Shopping:
    cart = []
    oringin = "China"

    def __init__(self, name, location):
        self.name = "jamiu"
        self.location = "Dhaka"
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"Buying {item} for price {price}. Money given: {amount}. Remaining (change): {remaining}")

bosundhara = Shopping("Bosundhora", 'Dhaka')
bosundhara.purchase("lungi", 2323, 3000)






