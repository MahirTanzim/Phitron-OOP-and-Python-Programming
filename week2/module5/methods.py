

class phone:
    price = 120000
    color = "black"
    brand = "samsung"
    def call(self):
        print("I am calling him now")
        return 'call ended' 
    def message(self, phn_number, message):
        text = f"seding message to {phn_number} with message {message}"
        return text
    
my_phone = phone()
print(my_phone.price)
print(my_phone.color)
print(my_phone.brand)
my_phone.call()
print(my_phone.message(1234567890, "Hello! How are you?"))
# The above code defines a class `phone` with attributes and methods.