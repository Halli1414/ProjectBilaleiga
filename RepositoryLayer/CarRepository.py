# this is the CarRepository class
from models.Vehicles import Vehicle

class VehicleRepository:
    def __init__(self):
        self.__Vehicle = []

    def add_Vehicle(self, Vehicle):
        with open("/Data/vehicle.txt","a+") as Vehicle_file:
            Manufacturer = Vehicle.get_Manufacturer()
            Model = Vehicle.get_Model()
            id = Vehicle.get_Id()
            Color = Vehicle.get_Color()
            VehicleStatus = Vehicle.get_VehicleStatus()
            Kilometers = Vehicle.get_Kilometers()
            Vehicle_file.write("{},{},{},{},{},{}\n".format(Manufacturer, Model,id, Color, VehicleStatus, Kilometers))
    
    def getVehicle(self):
        if self.__Vehicle == []:
            with open("./Data/Vehicle.txt", "r") as Vehicle_file:
                for line in Vehicle_file.readlines():
                    Manufacturer, Model, id, Color, VehicleStatus, Kilometers = line.split(",")
                    new_Vehicle = Vehicle(Manufacturer, Model, id, Color, VehicleStatus, Kilometers)
                    self.__Vehicle.append(new_Vehicle)
        return self.__Vehicle


