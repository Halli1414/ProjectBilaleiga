# this is the VehicleService class
from RepositoryLayer.VehicleRepository import VehicleRepository
from Models.Vehicle import Vehicle

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
            if vehicle.getVehicleStatus() == "1":
                return_vehicle = vehicle
        return return_vehicle
    
    def allUnavailable(self):
        return_vehicle = None
        for vehicle in self.__vehicles:
            if vehicle.getVehicleStatus() == "2":
                return_vehicle = vehicle
        return return_vehicle
    
    def getNextAvailable(self, category):
        return_vehicle = None
        for vehicle in self.__vehicles:
            if vehicle.getVehicleStatus() == "1":
                if vehicle.getCategory() == category:
                    return_vehicle = vehicle
        return return_vehicle
    
    def returnVehicle(self, id):
        returnVehicle = None 
        for vehicle in self.__vehicles:
            returnVehicle = input("ID: ")
            if returnVehicle == "2":
                returnVehicle = "1"
            elif returnVehicle == "1":
                print("Vehicle is already available")

    def list_up_to_date(self):
        if self.__vehicles == []:
            self.__vehicles = self.__vehicle_repo.getVehicle()

