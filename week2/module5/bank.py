class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.mn = 500
        self.mx = 50000
        
    
    def currentBalance(self):
        print(f"Your current balance is {self.balance} Taka")
    
    def deposit(self, amount):
        if amount < self.mn:
            print(f"You can't Deposit less than {self.mn} Taka")
        elif amount > self.mx:
            print(f"You can't deposit more than {self.mx} Taka")
        else:
            self.balance += amount
            print(f"You have successfully deposit {amount} Taka.")
            print(f"Your current Balance is {self.balance} Taka")

    def withdraw(self, amount):
        if amount < self.mn:
            print(f"You can't withraw less than {self.mn} Taka")
        elif amount > self.mx:
            print(f"You can't withraw more than {self.mx} Taka")
        else:
            self.balance -= amount
            print(f"You have successfully withraw {amount} Taka.")
            print(f"Your current Balance is {self.balance} Taka")

mahir = Bank(25000)
while True:
    print("Welcome Mahir\nTo See Balance: 1\nTo Deposit: 2\nTo withdraw: 3")
    x = int(input())
    if x == 1:
        mahir.currentBalance()
    elif x == 2: 
        amount = int (input("How much you want to Deposit: "))
        mahir.deposit(amount)
    elif x == 3: 
        amount = int (input("How much you want to Withdraw: "))
        mahir.withdraw(amount)
    
    print('Press any key to exit')
    i = input()