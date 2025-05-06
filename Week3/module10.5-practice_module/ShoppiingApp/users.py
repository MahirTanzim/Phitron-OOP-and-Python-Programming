# user class --> seller, buyer
class User:
    def __init__(self, name, email, phone, address, passward):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.passward = passward
        
class Seller(User):
    def __init__(self, name, email, phone, address, passward):
        super().__init__(name, email, phone, address, passward)

    def create_account(self, shop, seller):
        shop.create_seller_account(self, seller)
    
    def add_product(self, shop, product):
        shop.add_product(product)


    
    


class Buyer(User):


    

