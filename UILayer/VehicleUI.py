
from ServiceLayer.VehicleService import VehicleService
from Models.Vehicle import Vehicle

class VehicleUI:

    def __init__(self):
        self.__vehicle_service = VehicleService()
        self.__choice = ""
        self.__selectedVehicle = None

    def getSelected(self):
        return self.__selectedVehicle

    def start(self):
        while self.__choice != "q":
            self.printMenu()
            self.__choice = self.getInput().lower()
            if self.__choice == "1":
                self.findVehicles()
            elif self.__choice == "2":
                self.allVehicles()
            elif self.__choice == "3":
                self.allAvailable()
            elif self.__choice == "4":
                self.allUnavailable()
            elif self.__choice == "5":
                self.addVehicle() 

    def printMenu(self):
        print("1.Find vehicle")
        print("2.All vehicles")
        print("3.All available")
        print("4.All unavailable")
        print("5.Add vehicle")
        

    def findVehicles(self):
        vehicle_id = input("ID: ")
        vehicle = self.__vehicle_service.findVehicle(vehicle_id)
        print("vehicle: ", vehicle)


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
        vehicle_id = input("ID: ")
        model = input("Model: ")
        manufacturer = input("Manufacturer: ")
        color = input("Color: ")
        vehicleStatus = input("VehicleStatus: ")
        kilometers = input("Kilometers: ")
        category = input("Category: ")
        new_vehicle = vehicle(
            vehicle_id, model, manufacturer, color, vehicleStatus, kilometers, category
            )

    def getInput(self):
        return input()
    
    def getNextAvailable(self, category):
        return self.__vehicle_service.getNextAvailable(category)
