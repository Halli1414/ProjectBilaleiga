
from ServiceLayer.VehicleService import VehicleService
from Models.Vehicle import Vehicle

class VehicleUI:

    def __init__(self):
        self.__vehicle_service = VehicleService()
        self.__choice = ""

    def start(self):
        while self.__choice != q:
            self.printMenu()
            self.__choice = self.getInput().lower()

            if self.__choice == "1":
                self.FindVehicle()
            elif self.__choice == "2":
                self.allVehicles()
            elif self.__choice == "3":
                self.__allAvailable()
            elif self.__choice == "4":
                self.__allUnavailable()
            elif self.__choice == "5":
                self.__addVehicle() 

    def printMenu(self):
        print("1.Find vehicle")
        print("2.All vehicles")
        print("3.All available")
        print("4.All unavailable")
        print("5.Add vehicle")
        

    def findVehicles(self, search_term):
        Vehicle_id = input("ID: ")
        self.__vehicle_service.FindVehicles(search_term)

    def allVehicles(self):
        self.__vehicle_service.getVehicle()

    def allAvailable(self):
        availableVehicles = self.__vehicle_service.allAvailable()
        for vehicle in availableVehicles:
            print(vehicle)
            
    def allUnavailable(self):
        unavailableVehicles = self.__vehicle_service.allUnavailable()
        for vehicle in unavailableVehicles:
            print(vehicle)



    def addVehicle(self):
        Vehicle_id = input("ID: ")
        Model = input("Model: ")
        Manufacturer = input("Manufacturer: ")
        Color = input("Color: ")
        VehicleStatus = input("VehicleStatus: ")
        Kilometers = input("Kilometers: ")
        new_vehicle = Vehicle(
            Vehicle_id, Model, Manufacturer, Color, VehicleStatus, Kilometers
            )
