# this is the VehicleRepository class
from Models.Vehicle import Vehicle

class VehicleRepository:
    def __init__(self):
        self.__Vehicle = []

    def addVehicle(self, Vehicle):
        with open("./Data/vehicles.txt","a+") as Vehicle_file:
            Manufacturer = Vehicle.getManufacturer()
            Model = Vehicle.getModel()
            id = Vehicle.getID()
            Color = Vehicle.getColor()
            VehicleStatus = Vehicle.getVehicleStatus()
            Kilometers = Vehicle.getKilometers()
            Category = Vehicle.getCategory()
            Vehicle_file.write("{},{},{},{},{},{},{}\n".format(Manufacturer, Model,id, Color, VehicleStatus, Kilometers, Category))
    
    def getVehicle(self):
        if self.__Vehicle == []:
            with open("./Data/vehicles.txt", "r") as vehicle_file:
                for line in vehicle_file.readlines():
                    line = line.strip("\n")
                    Manufacturer, Model, vehicle_id, Color, VehicleStatus, Kilometers, Category = line.split(",")
                    new_Vehicle = Vehicle(Manufacturer, Model, vehicle_id, Color, VehicleStatus, Kilometers, Category)
                    self.__Vehicle.append(new_Vehicle)
        return self.__Vehicle

    def clearVehicle(self):
        with open("./Data/vehicles.txt","w") as vehicle_file:
            vehicle_file.write("")

    def deleteVehicle(self, Vehicle):
        self.clearVehicle()
        with open("./Data/vehicles.txt","a+") as vehicle_file:
            for Vehicle in vehicle_file:
                Manufacturer = Vehicle.getManufacturer()
                Model = Vehicle.getModel()
                id = Vehicle.getID()
                Color = Vehicle.getColor()
                VehicleStatus = Vehicle.getVehicleStatus()
                Kilometers = Vehicle.getKilometers()
                Category = Vehicle.getCategory()
                vehicle_file.write("{},{},{},{},{},{},{}\n".format(Manufacturer,Model,id, Color, VehicleStatus, Kilometers, Category))
            


