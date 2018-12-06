# this is the VehicleService class

class VehicleService(object):
    def __init__(self):
        self.__vehicle_repo = VehicleRepository()

    def add_Vehicle(self, Vehicle):
        self.__vehicle_repo.add_Vehicle(Vehicle)
    
    def get_Vehicle(self):
        return self.__vehicle_repo.get_Vehicle()


