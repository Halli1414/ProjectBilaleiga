
from 

class VehicleUi:

    def __init__(self):
        self.__vehicle_service = VehicleService()


    def main(self):

        action = ""
        print("1.Find Vehicle")
        print("2.All Vehicles")
        print("3.All Available")
        print("4.All Unavailable")

        action = input("Choose an option")

    def FindVehicles(self):
        Vehicle_id = input("ID: ")
        Model = input("Model: ")
        Manufacturer = input("Manufacturer: ")
        Color = input("Color: ")

        FindVehicles = Vehicles(Vehicle_id, Model, Manufacturer, Color)
        






