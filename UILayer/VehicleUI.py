
from 

class VehicleUi:

    def __init__(self):
        self.__vehicle_service = VehicleService()


    def printMenu(self):
        print("1.Find Vehicle")
        print("2.All Vehicles")
        print("3.All Available")
        print("4.All Unavailable")
        print("5.Add Vehicle")
        

    def FindVehicles(self):
        self.__vehicle_service.FindVehicles(search_term)

    def allVehicles(self):
        

    def allAvailable(self):
    

    def allUnavailable(self):



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
