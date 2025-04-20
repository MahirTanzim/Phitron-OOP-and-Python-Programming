
# base class, parent class, or super class, common attributes and methods class
# derived class, child class, or sub class, specific attributes and methods class

class Device:   # base class, parent class, or super class, common attributes and methods class
    def __init__ (self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self): 
        return f"Running {self.brand} device."

    
    
class Laptop:       
    def __init__ (self, ram, storage):
        self.ram = ram
        self.storage = storage

    def run(self):
        return f"Running {self.brand} laptop with {self.ram}GB RAM and {self.storage}GB storage."
    
    def codindg(self):
        return f"{self.brand} laptop is great for coding."


class Phone(Device): #  inheriting from Device class
    # constructor of child class
    def __init__ (self, brand, price, color, dual_sim, ram, storage):
        self.ram = ram
        self.storage = storage
        self.dual_sim = dual_sim
        super().__init__(brand, price, color) # calling the constructor of parent class
        # Device.__init__(self, brand, price, color) # another way to call the constructor of parent class
        
    def call(self):
        return f"Calling from {self.brand} phone with {self.ram}GB RAM and {self.storage}GB storage."
   
    def gaming(self):
        print(f"{self.brand} phone is great for gaming.")
    
    def __repr__(self):
        return f"Phone(brand={self.brand}, price={self.price}, color={self.color}, dual_sim={self.dual_sim}, ram={self.ram}, storage={self.storage})"


class Camara:
    def __init__ (self, lens_type, megapixels):
        self.lens_type = lens_type
        self.megapixels = megapixels
  
    def change_lens(self, new_lens_type):
        self.lens_type = new_lens_type
        return f"Changed lens to {self.lens_type}."
    

    def click(self):
        return f"Clicking photos with {self.brand} camera with {self.megapixels}MP and {self.lens_type} lens."
    
    def video(self):
        return f"{self.brand} camera is great for video recording."


myphone = Phone("Samsung", 1000, "Black", True, 8, 128)

print(myphone.call())
print(myphone.gaming())
print(myphone.run())

d = Device("Dell", 1500, "Silver")

print(myphone)