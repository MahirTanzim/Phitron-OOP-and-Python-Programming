

class phone:
    price = 120000
    color = "black"
    brand = "samsung"
    def call(self):
        print("I am calling him now")
        return 'call ended' 
    
my_phone = phone()
print(my_phone.price)
print(my_phone.color)
print(my_phone.brand)
my_phone.call()