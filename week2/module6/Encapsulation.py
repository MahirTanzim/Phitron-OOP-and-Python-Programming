class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def getbalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance+=amount
    



mahir = Bank("Mahir", 40000)
print(mahir.name)
print(mahir.getbalance())
mahir.deposit(100)
print(mahir.getbalance())

