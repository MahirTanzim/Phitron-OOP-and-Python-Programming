
from datetime import datetime
class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
    def set_driver(self, driver):
        self.driver = driver
        
    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare


    def __repr__(self):
        return f'''Ride Details
        Start : {self.start_location}\tTime : {self.start_time}
End : {self.end_location}\tTime : {self.end_time}
Amount : {self.estimated_fare}
        '''
    

class RideRequest:
    def __init__(self, rider, ride_location):
        self.rider = rider
        self.ride_location = ride_location

class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        