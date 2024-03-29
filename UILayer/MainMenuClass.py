from UILayer.CustomerUI import CustomerUI
from UILayer.OrderUI import OrderUI
from UILayer.VehicleUI import VehicleUI

# This is the ui class that handles all of the menus

class MainMenu:
    def __init__(self):
        self.__customer_ui = CustomerUI()
        self.__order_ui = OrderUI()
        self.__vehicle_ui = VehicleUI()
        self.__selected_order = None
        self.__selected_vehicle = None
        self.__selected_customer = None
        self.__choice = ""

    def start(self):
        while self.__choice.lower() != "exit":
            self.printMainMenu()
            self.__choice = self.getInput()
            # Order menu
            if self.__choice == "1":
                while self.__choice != "q":
                    self.__order_ui.printMenu()
                    self.__choice = self.getInput()
                    # New order
                    # Virkar 100%
                    if self.__choice == "1":
                        self.addOrder()
                    # Find order
                    # Virkar 100%
                    elif self.__choice == "2":
                        self.findOrder()
                    # All orders
                    elif self.__choice == "3":
                        self.allOrders()
                    # Update order
                    # Virkar 100%
                    elif self.__choice == "4":
                        self.updateOrder()
                    # Delete order
                    # Virkar 100%
                    elif self.__choice == "5":
                        self.deleteOrder()
            # Customer menu
            elif self.__choice == "2":
                while self.__choice != "q":
                    self.__customer_ui.printMenu()
                    self.__choice = self.getInput()
                    # New customer
                    if self.__choice == "1":
                        self.__customer_ui.newCustomer()
                    # Find customer
                    elif self.__choice == "2": 
                        self.__selected_customer = self.__customer_ui.findCustomer()
                        self.__customer_ui.printCustomerResaults(
                            self.__selected_customer
                        )
                    # All customer
                    elif self.__choice == "3":
                        self.__customer_ui.allCustomers()
                    # Update customer
                    elif self.__choice == "4":
                        if self.customerConfirm() != "q":
                            self.__customer_ui.updateCustomer(
                                self.__selected_customer
                                )
                    # Delete customer
                    elif self.__choice == "5":
                        if self.__selected_customer == None:
                            print("No selected customer.")
                            self.otherCustomerOptions()
                        #Customer selected, user asked whether to use selected
                                               
                        self.__choice = self.customerConfirm()
                        while self.__choice != "y":
                            self.otherCustomerOptions()
                            self.__choice = self.customerConfirm()
                        self.__customer_ui.deleteCustomer()
                self.__selected_customer = self.__customer_ui.getSelected()
            #Vehicle menu
            elif self.__choice == "3":
                while self.__choice != "q":
                    self.__vehicle_ui.printMenu()
                    self.__choice = self.getInput()
                    if self.__choice == "1":
                        self.__vehicle_ui.findVehicle()
                    elif self.__choice == "2":
                        resaults = self.__vehicle_ui.allVehicles()
                        self.__vehicle_ui.printVehicleResaults(resaults)
                    elif self.__choice == "3":
                        self.__vehicle_ui.allAvailable()
                    elif self.__choice == "4":
                        self.__vehicle_ui.allUnavailable()
                    elif self.__choice == "5":
                        self.__vehicle_ui.addVehicle()
                    elif self.__choice == "6":
                        self.__vehicle_ui.returnVehicle()
                    elif self.__choice == "7":
                        self.__vehicle_ui.deleteVehicle()
                    elif self.__choice == "8":
                        self.__vehicle_ui.printVehiclePrices()
                self.__selected_vehicle = self.__vehicle_ui.getSelected()

    def getInput(self, prompt=""):
        return input(prompt)

    def printMainMenu(self):
        print ("\n" * 100)
        print("Enter (exit) to quit.")
        print("'RENT-A-CAR'")
        print("(1) Orders")
        print("(2) Customer")
        print("(3) Vehicles")

    def otherCustomerOptions(self):
        print("1. Register new customer")
        print("2. Find customer")
        print("3. List all customers")
        choice = self.getInput().lower()
        if choice == "1":
            self.__customer_ui.newCustomer()
        elif choice == "2":
            self.__customer_ui.findCustomer()
        elif choice == "3":
            self.__customer_ui.allCustomers()

        self.__selected_customer = self.__customer_ui.getSelected()

    def otherVehicleOptions(self):
        self.__selected_vehicle = self.__vehicle_ui.getNextAvailableVehicle()

    def otherOrderOptions(self):
        print("1. Make new order")
        print("2. Find order")
        print("3. List all orders")
        choice = self.getInput().lower()

        if choice == "1":
            self.addOrder()
        elif choice == "2":
            self.findOrder()
        elif choice == "3":
            self.allOrders()

    def customerConfirm(self):
        if self.__selected_customer == None:
            print("No selected customer.")
            self.otherCustomerOptions()

        print(self.__selected_customer)
        print("Use selected customer?(Y/N)")
                
        choice = self.getInput().lower()
        if choice != "q":
            while choice != "y":
                self.otherCustomerOptions()
                choice = self.customerConfirm()
                if choice.lower() == "q":
                    break
        return choice
        
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
            if choice.lower() == "q":
                break
        return choice

    def orderConfirm(self):
        if self.__selected_order == None:
            print("No selected order.")
            self.otherOrderOptions()

        print(self.__selected_order)
        print("Use selected order?(Y/N)")

        choice = self.getInput().lower()
        while choice != "y":
            self.otherOrderOptions()
            choice = self.orderConfirm()
            if choice.lower() == "q":
                break
        self.__selected_customer = self.__selected_order.getCustomer()
        self.__selected_vehicle = self.__selected_order.getVehicle()
        return choice


    def addOrder(self):         
        self.customerConfirm()
        self.vehicleConfirm()
        self.__order_ui.newOrder(
            self.__selected_customer, self.__selected_vehicle
            )
        self.__selected_order = self.__order_ui.getSelected()
        # self.__vehicle_ui.changeVehicleStatus(
        #     self.__selected_vehicle.getID(), "2"
        #     )

    def findOrder(self):
        self.__selected_order = self.__order_ui.findOrder()
        self.__order_ui.printOrderResaults(self.__selected_order)

    def allOrders(self):
        resaults = self.__order_ui.allOrders()
        self.__order_ui.printOrderResaults(resaults)

    def updateOrder(self):
        self.orderConfirm()
        self.customerConfirm()
        self.vehicleConfirm()

        self.__order_ui.updateOrder(
            self.__selected_order, self.__selected_customer, self.__selected_vehicle
            )

    def deleteOrder(self):
        self.orderConfirm()
        self.__order_ui.deleteOrder(self.__selected_order.getID())
        self.__selected_order = self.__order_ui.getSelected()