#This is the class that handles Order menues
from ServiceLayer.OrderService import OrderService
from Models.Order import Order
from datetime import datetime


class OrderUI(object):

    def __init__(self):
        self.__order_service = OrderService()
        self.__choice = ""
        self.__selected_order = self.__order_service.getLastOrderID()

    # def start(self):
    #     while self.__choice != "q":
    #         self.printMenu()
    #         self.__choice = self.getInput().lower()

    #         if self.__choice == "1":
    #             self.newOrder()
    #         elif self.__choice == "2":
    #             search = self.getInput("Enter order ID")
    #             self.findOrder(search)
    #         elif self.__choice == "3":
    #             self.allOrders()
    #         elif self.__choice == "4":
    #             self.updateOrder()
    #         elif self.__choice == "5":
    #             self.deleteOrder()

    def printMenu(self):
        print("1. New order")
        print("2. Find order")
        print("3. All orders")
        print("4. Update order")
        print("5. Delete order")

    def newOrder(self, a_customer, a_vehicle):
        customer = a_customer
        vehicle = a_vehicle
        year, month, day = self.getInput("Start date(yyyy-mm-dd):").split("-")
        start_date = datetime(int(year), int(month), int(day)).date()
        year, month, day = self.getInput("End date(yyyy-mm-dd):").split("-")
        end_date = datetime(int(year), int(month), int(day)).date()
        payment = self.getInput("Payment")

        self.__selected_order = self.__order_service.addOrder(
            customer, vehicle, start_date, end_date, payment
            )

    def findOrder(self):
        order_id = self.getInput("Enter order ID")
        self.__selected_order = self.__order_service.findOrder(order_id)
        print(self.__selected_order)
        

    def allOrders(self):
        orders = self.__order_service.getOrders()
        for order in orders:
            print(order)

    def deleteOrder(self, selected_order):
        message = self.__order_service.deleteOrder(selected_order)
        print(message)

    def updateOrder(self, a_order, a_customer, a_vehicle):
        customer = a_customer
        vehicle = a_vehicle
        year, month, day = self.getInput("Start date(yyyy-mm-dd): ").split("-")
        start_date = datetime(int(year), int(month), int(day)).date()
        year, month, day = self.getInput("End date(yyyy-mm-dd): ").split("-") 
        end_date = datetime(int(year), int(month), int(day)).date()
        payment = self.getInput("Payment")

        self.__order_service.updateOrder(
            order_id, customer, vehicle, start_date, end_date, payment
            )

    def getInput(self, prompt=""):
        return input(prompt)
    
    def getSelected(self):
        return self.__selected_order

    def confirmDate(self):
        