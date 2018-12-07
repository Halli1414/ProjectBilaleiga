from ServiceLayer.CustomerService import CustomerService
from ServiceLayer.OrderService import OrderService
from ServiceLayer.VehicleService import VehicleService
#this is the ui class that handles all of the menus

class MainMenu:
    def __init__(self):
        self.__vehicle_service = VehicleService()
        self.__customer_service = CustomerService()
        self.__order_service = OrderService()
        self.__choice = ""

    def start(self):
        while self.__choice.lower() != "q":
            self.printMainMenu()
            self.__choice = self.getInput()
            if self.__choice == "1":
                self.printOrderMenu()
                self.__choice = self.getInput()
                if self.__choice.lower() == "a":
                    #runNewOrderFunction
                elif self.__choice.lower() == "b":
                    #runFindOrderFunction
                elif self.__choice.lower() == "c":
                    #runAllOrdersFunction
    def getInput(self, prompt=""):
        return input(prompt)

    def printScreen(self):
        self.printMainMenu()
       # return Menu????

    def printMainMenu(self):
        print ("\n" * 100)
        print("(Enter (q) to quit).")
        print("'RENT-A-CAR'")
        print("(1) Orders")
        print("(2) Customer")
        print("(3) Vehicles")

    def printOrderMenu(self):
        print("-- (a) New Order.")
        print("-- (b) Find Order.")
        print("-- (c) All Orders.")
    
    def printFindOrderMenu(self):
        print("---- (d) Update Order.")
        print("---- (e) Delete Order")
    
    def printCustomerMenu(self):
        print("-- (a) New Customer.")
        print("-- (b) Find Customer.")
        print("-- (c) All Customers.")

    def printVehicleMenu(self):
        print("--- (a) New Vehicle.")
        print("--- (b) Find Vehicle.")
        print("--- (c) All Vehicle.")