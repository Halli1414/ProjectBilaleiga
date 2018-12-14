# This is the class that handles Order menues
from ServiceLayer.OrderService import OrderService
from Models.Order import Order
from datetime import datetime


class OrderUI(object):

    def __init__(self):
        self.__order_service = OrderService()
        self.__selected_order = self.__order_service.getLastOrderID()

    def printMenu(self):
        print("1. New order")
        print("2. Find order")
        print("3. All orders")
        print("4. Update order")
        print("5. Delete order")

    def newOrder(self, a_customer, a_vehicle):
        customer = a_customer
        vehicle = a_vehicle
        print("Start date:")
        start_date = self.pickDate()
        print("End date:")
        end_date = self.pickDate()

        # Send values down do the serviceLayer to create Order
        self.__selected_order = self.__order_service.addOrder(
            customer, vehicle, start_date, end_date
            )

    def findOrder(self):
        order_id = self.getInput("Enter order ID")
        # Catch the order that was found and make it selected
        self.__selected_order = self.__order_service.findOrder(order_id)
        print(self.__selected_order)
        

    def allOrders(self):
        orders = self.__order_service.getOrders()
        for order in orders:
            print(order)

    def deleteOrder(self, selected_order_id):
        # Message varaible to print out the resaults, success or not
        message = self.__order_service.deleteOrder(selected_order_id)
        print(message)

    def updateOrder(self, a_order, a_customer, a_vehicle):
        # Initialize values
        order_id = a_order.getID()
        customer = a_customer
        vehicle = a_vehicle
        start_date = a_order.getOrderStartDate()
        end_date = a_order.getOrderEndDate()

        # Confirm whether to use dates or set new
        start_date = self.selectDate(start_date)
        end_date = self.selectDate(end_date, False)

        # Update order
        self.__order_service.updateOrder(
            order_id, customer, vehicle, start_date, end_date
            )

    def getInput(self, prompt=""):
        return input(prompt)
    
    def getSelected(self):
        return self.__selected_order

    # Prompt to the user to keep or change the dates
    def confirmDate(self, date, first=True):
        print(date)
        if first == True:
            print("Use this start date?(Y/N)")
        else:
            print("User this end date?(Y/N)")

        return self.getInput().lower()

    # In case of date change
    def selectDate(self, date, first=True):
        new_date = date
        choice = self.confirmDate(new_date, first)
        while choice != "y":
            new_date = self.pickDate()
            choice = self.confirmDate(new_date, first)
            
        return new_date


    def pickDate(self):
        year = self.getInput("Pick year. (yyyy)")
        month = self.getInput("Pick month. (mm)")
        day = self.getInput("Pick day. (dd)")
        return datetime(int(year), int(month), int(day)).date()

        