# this is the VehicleRepository class
from Models.Vehicle import Vehicle

class VehicleRepository:
    def __init__(self):
        self.__Vehicle = []

    def addVehicle(self, Vehicle):
        with open("./Data/vehicles.txt","a+") as Vehicle_file:
            Manufacturer = Vehicle.get_Manufacturer()
            Model = Vehicle.get_Model()
            id = Vehicle.get_Id()
            Color = Vehicle.get_Color()
            VehicleStatus = Vehicle.get_VehicleStatus()
            Kilometers = Vehicle.get_Kilometers()
            Vehicle_file.write("{},{},{},{},{},{}\n".format(Manufacturer, Model,id, Color, VehicleStatus, Kilometers))
    
    def getVehicle(self):
        if self.__Vehicle == []:
            with open("./Data/vehicles.txt", "r") as vehicle_file:
                for line in vehicle_file.readlines():
                    Manufacturer, Model, id, Color, VehicleStatus, Kilometers = line.split(",")
                    new_Vehicle = Vehicle(Manufacturer, Model, id, Color, VehicleStatus, Kilometers)
                    self.__Vehicle.append(new_Vehicle)
        return self.__Vehicle


