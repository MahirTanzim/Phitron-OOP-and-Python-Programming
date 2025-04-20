class shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, "quantity": quantity}
        self.cart.append(product)

    
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += (item['price']*item['quantity'])
        
        print(total)
        if total > amount:
            print(f"You Have to give more {total-amount} Taka")
        else:
            print(f"Here is your item and extra {amount - total} Taka")
        pass
    

mahir = shopping('Mahir')
mahir.add_to_cart('alu', 40, 4)
mahir.add_to_cart('dim', 12, 24)
mahir.add_to_cart('rice', 50, 6)

print(mahir.cart)

for item in mahir.cart:
    print(item)

mahir.checkout(1000)