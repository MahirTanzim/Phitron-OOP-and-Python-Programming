class shop:
    cart  = []      # cart is an class attribute
    def __init__(self, buyer):
        self.buyer = buyer

    def addtocart(self, item):
        self.cart.append(item)
    

maisha = shop("Maisha")
maisha.addtocart("iphone")
maisha.addtocart("Charger")

mahir = shop("Mahir")
mahir.addtocart("Headphone")
mahir.addtocart("T-Shirt")

print(mahir.cart)
print(maisha.cart)