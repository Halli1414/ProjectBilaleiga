from ServiceLayer.CustomerService import CustomerService
from ServiceLayer.OrderService import OrderService
#from ServiceLayer.VehicleSevice import VehicleSevice
#this is the ui class that handles all of the menus

class MainMenu:
    def __init__(self):
        #self.__vehicle_service = VehicleService()
        self.__customer_service = CustomerService()
        self.__order_service = OrderService()
        self.__choice =""

    def start(self):
        while self.__choice.lower() != "q":
            self.printMainMenu()
            self.__choice = self.getInput()
            
    def getInput(self, prompt=""):
        return input(prompt)

    def printScreen(self):
        self.printMainMenu()
       # return Menu????

    def printMainMenu(self):
        print("Project Bilaleiga")
        print("1.Orders")
        print("2.Customer")
        print("3.Vehicles")