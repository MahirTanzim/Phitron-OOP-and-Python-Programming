#shop class -> use it as database, contain the login, signin, order function 

class Shop:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.sellers = []  # contain Seller object
        self.buyer = []    # contain buyer object
        self.product = []

    def create_seller_account(self, seller):
        self.sellers.append(seller)
    
    def create_buyer_account(self, buyer):
        self.buyer.append(buyer)
    
    def add_product(self, product):
        self.products.append(product)

    @staticmethod
    def seller_login(id, passward):
        pass
    
    @staticmethod
    def buyer_login(id, passward):
        pass
    
        