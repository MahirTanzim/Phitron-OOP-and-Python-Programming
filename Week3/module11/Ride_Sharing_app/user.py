from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet  = initial_amount
        self.current_ride = None


    def display_profile(self):
        print(f"Rider : {self.name} email : {self.email}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Amount is less then 0")

    def update_location(self, current_location):
        self.current_location = current_location


    def request_ride(self, ride_sharing, destination):
        pass
    
    def show_current_ride(self):
        print(self.current_ride)


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"Driver Name: {self.name}")

    def accept_ride(self, ride):
        pass
    