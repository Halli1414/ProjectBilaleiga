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
        print("8.Vehicle prices")
        
    def findVehicle(self):
        vehicle_id = input("ID: ")
        vehicle = self.__vehicle_service.findVehicle(vehicle_id)
        self.__selected_vehicle = vehicle
        return vehicle

    def allVehicles(self):
        return self.__vehicle_service.getVehicles()

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
        manufacturer = input("Manufacturer: ")
        model = input("Model: ")
        color = input("Color: ")
        vehicleStatus = input("VehicleStatus: ")
        kilometers = input("Kilometers: ")
        category = input("Category: ")
        new_vehicle = Vehicle(
            manufacturer, model, vehicle_id, color, vehicleStatus, kilometers, category
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
        print("1. Get next available")
        print("2. Find specific")
        print("3. List all vehicles")
        
        choice = self.getInput().lower()
        if choice == "1":
            return self.getNextAvailableVehicle()
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
        return self.__selected_vehicle

    def printVehicleHeader(self):
        print("\n" * 100)
        print("{:<5}{:<10}{:<20}{:<20}{:<10}{:<15}{:<15}{:<15}".format(
            "No.", "ID", "Manufacturer", "Model", "Color", "Kilometers", "Status", "Category"
            ))

    def printVehicleList(self, vehicle_list):
        self.printVehicleHeader()
        for i in range(0, len(vehicle_list)):
            print("{:>3}. {}".format(i+1, self.printVehicle(vehicle_list[i])))
        input("Press (Enter) to continue.")
    
    def printVehicle(self, vehicle):

        status = self.parseStatus(vehicle.getVehicleStatus())
        category = self.parseCategory(vehicle.getCategory())
        return "{:.<10}{:.<20}{:.<20}{:.<10}{:.<15}{:.<15}{:<15}".format(
            vehicle.getID(), vehicle.getManufacturer(), vehicle.getModel(), vehicle.getColor(), vehicle.getKilometers(), status, category
            )

    def printVehicleResaults(self, resaults):
        resaults_list = []
        if type(resaults) == list:
            resaults_list = resaults
        elif type(resaults) == Vehicle:
            resaults_list.append(resaults)
        self.printVehicleList(resaults_list)

    def printVehiclePrices(self):
        print("\n" * 100)
        print("{:<10}{:<10}\n{:<10}{:<10}\n{:<10}{:<10}\n".format("Small:", "5.900kr", "Medium:", "9.900kr", "Large:", "12.900kr"))

    def parseCategory(self, category):
        if category == "1":
            return "Small"
        elif category == "2":
            return "Medium"
        elif category == "3":
            return "Large"

    def parseStatus(self, status):
        if status == "1":
            return "Available"
        elif status == "2":
            return "Unavailable"