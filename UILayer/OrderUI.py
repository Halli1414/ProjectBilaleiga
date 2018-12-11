#This is the class that handles Order menues
from ServiceLayer.OrderService import OrderService
from Models.Order import Order


class OrderUI(object):

    def __init__(self):
        self.__order_service = OrderService()

    def printMenu(self):
        print("1. New order")
        print("2. Find order")
        print("3. All orders")
        print("4. Update order")
        print("5. Delete order")

    def newOrder(self):
        customer = self.getInput("Customer: ")
        vehicle = self.getInput("Vehicle: ")
        start_date = self.getInput("Start date(yyyy/mm/dd): ")
        end_date = self.getInput("End date(yyyy/mm/dd): ")
        payment = self.getInput("Payment")

        new_order = Order(customer, vehicle, start_date, end_date, payment)
        self.__order_service.addOrder(new_order)

    def findOrder(self, search_term):
        #self.__order_service.findOrder(search_term)
        pass


    def getInput(self, prompt):
        return input(prompt)