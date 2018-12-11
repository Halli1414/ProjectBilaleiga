#from UILayer.CustomerUI import CustomerUI
from UILayer.OrderUI import OrderUI
#from UILayer.VehicleUI import VehicleUI

from ServiceLayer.CustomerService import CustomerService
from ServiceLayer.OrderService import OrderService
from ServiceLayer.VehicleService import VehicleService

#this is the ui class that handles all of the menus

class MainMenu:
    def __init__(self):
        #self.__customer_ui = CustomerUI()
        self.__order_ui = OrderUI()
        #self.__vehicle_ui = VehicleUI()
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
                    #run new order function here.
                    pass
                elif self.__choice.lower() == "b":
                    #run find order function here.
                    self.printFindOrderMenu()
                    self.__choice = self.getInput()
                    if self.__choice.lower() == "d":
                        #run update order function here.
                        pass
                    if self.__choice.lower() == "e":
                        #run delete order function here.
                        pass
                elif self.__choice.lower() == "c":
                    #run all orders function here.
                    self.__order_ui.printMenu()
                    self.__choice = self.getInput()
            elif self.__choice == "2":
                self.printCustomerMenu()
                self.__choice = self.getInput()
                if self.__choice.lower() == "a":
                    #run new customer function here.
                    pass
                elif self.__choice.lower() == "b":
                    #run find customer function here.
                    self.printFindCustomerMenu()
                    self.__choice = self.getInput()
                    if self.__choice.lower() == "d":
                        #run update customer function here.
                        pass
                    elif self.__choice.lower() == "e":
                        #run delete customer function here.
                        pass
                elif self.__choice.lower() == "c":
                    #run all customers function here.
                    pass
            elif self.__choice == "3":
                self.printVehicleMenu()
                self.__choice = self.getInput()
                if self.__choice.lower() == "a":
                    #run new vehicle function here.
                    pass
                elif self.__choice.lower() == "b":
                    #run find vehicle function here.
                    self.printFindVehicleMenu()
                    self.__choice = self.getInput()
                    if self.__choice.lower() == "d":
                        #run update vehicle function here.
                        pass
                    elif self.__choice.lower() == "e":
                        #run delete vehicle function here.
                        pass
                elif self.__choice.lower() == "c":
                    #run all vehicles function here.
                    pass

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
        self.printMainMenu()
        print("-- (a) New Order.")
        print("-- (b) Find Order.")
        print("-- (c) All Orders.")
    
    def printFindOrderMenu(self):
        self.printOrderMenu()
        print("---- (d) Update Order.")
        print("---- (e) Delete Order")
    
    def printCustomerMenu(self):
        self.printMainMenu()
        print("-- (a) New Customer.")
        print("-- (b) Find Customer.")
        print("-- (c) All Customers.")

    def printFindCustomerMenu(self):
        self.printCustomerMenu()
        print("---- (d) Update Customer.")
        print("---- (e) Delete Customer.")

    def printVehicleMenu(self):
        self.printMainMenu()
        print("-- (a) New Vehicle.")
        print("-- (b) Find Vehicle.")
        print("-- (c) All Vehicles.")

    def printFindVehicleMenu(self):
        self.printVehicleMenu()
        print("---- (d) Update Vehicle.")
        print("---- (e) Delete Vehicle.")