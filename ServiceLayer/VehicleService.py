# this is the VehicleService class

class VehicleService(object):
    def __init__(self):
        self.__vehicle_repo = VehicleRepository()
        self.__vehicles = []

    def addVehicle(self, Vehicle):
        self.__vehicle_repo.add_Vehicle(Vehicle)
    
    def getVehicle(self):
        return self.__vehicle_repo.get_Vehicle()

    def findAvailable(self, VehicleStatus):
        return_vehicle = None
        for vehicle in self.__vehicles:
            if vehicle.getStatus() == VehicleStatus:
                return_vehicle = Vehicle
        return return_vehicle
    
    def findUnavailable(self, VehicleStatus):
        return_vehicle = None
        for vehicle in self.__vehicles:
            if vehicle.getStatus() == VehicleStatus:
                return_vehicle = Vehicle
        return return_vehicle

