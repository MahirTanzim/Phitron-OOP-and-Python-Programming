
# Common and uncommon things and Inheritance
class Laptop:
    def __init__ (self, brand, price, color, ram, storage):
        self.brand = brand
        self.price = price
        self.color = color
        self.ram = ram
        self.storage = storage

    def run(self):
        return f"Running {self.brand} laptop with {self.ram}GB RAM and {self.storage}GB storage."
    
    def codindg(self):
        return f"{self.brand} laptop is great for coding."


class Phone:
    def __init__ (self, brand, price, color, dual_sim, ram, storage):
        self.brand = brand
        self.price = price
        self.color = color
        self.ram = ram
        self.storage = storage
        self.dual_sim = dual_sim

    def call(self):
        return f"Calling from {self.brand} phone with {self.ram}GB RAM and {self.storage}GB storage."
   
    def gaming(self):
        print(f"{self.brand} phone is great for gaming.")


class Camara:
    def __init__ (self, brand, price, color, lens_type, megapixels):
        self.brand = brand
        self.price = price
        self.color = color
        self.lens_type = lens_type
        self.megapixels = megapixels

    def run(self):
        return f"Running {self.brand} camera with {self.lens_type} lens and {self.megapixels}MP."
    
    def change_lens(self, new_lens_type):
        self.lens_type = new_lens_type
        return f"Changed lens to {self.lens_type}."
    

    def click(self):
        return f"Clicking photos with {self.brand} camera with {self.megapixels}MP and {self.lens_type} lens."
    
    def video(self):
        return f"{self.brand} camera is great for video recording."