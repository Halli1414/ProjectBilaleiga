# this is the VehicleService class
from RepositoryLayer.VehicleRepository import VehicleRepository

class VehicleService(object):
    def __init__(self):
        self.__vehicle_repo = VehicleRepository()
        self.__vehicles = self.__vehicle_repo.getVehicle()

    def addVehicle(self, Vehicle):
        self.__vehicle_repo.addVehicle(Vehicle)
    
    def getVehicle(self):
        return self.__vehicle_repo.getVehicle()

    def findVehicle(self, vehicle_id):
        return_vehicle = None
        for vehicle in self.__vehicles:
            if vehicle.getID() == vehicle_id:
                return_vehicle = vehicle
        return return_vehicle

    
    def allAvailable(self):
        return_vehicle = None
        for vehicle in self.__vehicles:
            if vehicle.getStatus() == "available":
                return_vehicle = vehicle
        return return_vehicle
    
    def allUnavailable(self):
        return_vehicle = None
        for vehicle in self.__vehicles:
            if vehicle.getStatus() == "unavailable":
                return_vehicle = vehicle
        return return_vehicle
    
    def getNextAvailable(self, catagory):
        return_vehicle = None
        for vehicle in self.__vehicles:
            if vehicle.getVehicleStatus() == "available":
                if vehicle.getCatagory() == catagory:
                    return_vehicle = vehicle
        return return_vehicle



