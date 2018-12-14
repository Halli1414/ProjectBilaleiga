from ServiceLayer.VehicleService import VehicleService
from Models.Vehicle import Vehicle

class VehicleUI:

    def __init__(self):
        self.__vehicle_service = VehicleService()
        self.__choice = ""
        self.__selected_vehicle = None

    def getSelected(self):
        return self.__selected_vehicle

    def printMenu(self):
        print("1.Find vehicle")
        print("2.All vehicles")
        print("3.All available")
        print("4.All unavailable")
        print("5.Add vehicle")
        print("6.Return vehicle")
        print("7.Delete vehicle")
        
    def findVehicle(self):
        vehicle_id = input("ID: ")
        vehicle = self.__vehicle_service.findVehicle(vehicle_id)
        self.__selected_vehicle = vehicle
        return vehicle

    #def print(self):
        

    def allVehicles(self):
        vehicles = self.__vehicle_service.getVehicle()
        for vehicle in vehicles:
            print(vehicle)

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
        new_vehicle = Vehicle(
            vehicle_id, model, manufacturer, color, vehicleStatus, kilometers, category
            )
        self.__vehicle_service.addVehicle(new_vehicle)

    def returnVehicle(self):
        print("Enter vehicle ID: ")
        vehicle_id = self.getInput()
        message = self.__vehicle_service.returnVehicle(vehicle_id)
        print(message)
    
    def deleteVehicle(self):
        if self.vehicleConfirm() != "q":
            self.__vehicle_service.deleteVehicle(self.__selected_vehicle)
        
        

    def getInput(self):
        return input()
    
    
    def vehicleConfirm(self):
        if self.__selected_vehicle == None:
            print("No selected Vehicle.")
            self.otherVehicleOptions()
        
        print(self.__selected_vehicle)
        print("Use selected vehicle?(Y/N)")

        choice = self.getInput().lower()
        while choice != "y":
            self.otherVehicleOptions()
            choice = self.vehicleConfirm()

        return choice

    def otherVehicleOptions(self):
        print("1. Get next avaliable")
        print("2. Find specific")
        print("3. List all vehicles")
        
        choice = self.getInput().lower()
        if choice == "1":
            self.getNextAvailableVehicle()
        elif choice == "2":
            self.findVehicle()
        elif choice == "3":
            self.allVehicles()

    def getNextAvailableVehicle(self):
        print("Vehicle category(1/2/3)?")
        category = self.getInput().lower()
        self.__selected_vehicle = self.__vehicle_service.getNextAvailable(
            category
            )