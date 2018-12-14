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
            self.refreshVehicleList()
        return self.__vehicles
            

    def clearVehicle(self):
        with open("./Data/vehicles.txt","w") as vehicle_file:
            vehicle_file.write("")

    def updateVehicleFile(self, vehicle_list):
        str_with_vehicles = ""
        with open("./Data/vehicles.txt","w") as vehicle_file:
            for Vehicle in vehicle_list:
                Manufacturer = Vehicle.getManufacturer()
                Model = Vehicle.getModel()
                Vehicle_id = Vehicle.getID()
                Color = Vehicle.getColor()
                VehicleStatus = Vehicle.getVehicleStatus()
                Kilometers = Vehicle.getKilometers()
                Category = Vehicle.getCategory()
                str_with_vehicles += "{},{},{},{},{},{},{}\n".format(Manufacturer,Model, Vehicle_id, Color, VehicleStatus, Kilometers, Category
                )
                vehicle_file.write(str_with_vehicles)
            
            self.refreshVehicleList()
    
    def refreshVehicleList(self):
        self.__vehicles = []
        with open("./Data/vehicles.txt", "r") as vehicle_file:
                for line in vehicle_file.readlines():
                    line = line.strip("\n")
                    Manufacturer, Model, vehicle_id, Color, VehicleStatus, Kilometers, Category = line.split(",")
                    new_Vehicle = Vehicle(Manufacturer, Model, vehicle_id, Color, VehicleStatus, Kilometers, Category)
                    self.__vehicles.append(new_Vehicle)

            


