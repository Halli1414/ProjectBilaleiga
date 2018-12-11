#This is the class that handles Order menues
from ServiceLayer.OrderService import OrderService
from Models.Order import Order


class OrderUI(object):

    def __init__(self):
        self.__order_service = OrderService()
        self.__choice = ""
        self.__selected_order = ""

    def start(self):
        while self.__choice != "q":
            self.printMenu()
            self.__choice = self.getInput().lower()

            if self.__choice == "1":
                self.newOrder()
            elif self.__choice == "2":
                search = self.getInput("Enter order ID")
                self.findOrder(search)
            elif self.__choice == "3":
                self.allOrders()
            elif self.__choice == "4":
                self.updateOrder()
            elif self.__choice == "5":
                self.deleteOrder()

    def printMenu(self):
        print ("\n" * 100)
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

        new_order = Order(id, customer, vehicle, start_date, end_date, payment)
        self.__order_service.addOrder(new_order)

    def findOrder(self, order_id):
        self.__selected_order = self.__order_service.findOrder(order_id)
        print(self.__selected_order)
        

    def allOrders(self):
        self.__order_service.getOrders()

    def deleteOrder(self):
        pass

    def updateOrder(self):
        customer = self.getInput("Customer: ")
        vehicle = self.getInput("Vehicle: ")
        start_date = self.getInput("Start date(yyyy/mm/dd): ")
        end_date = self.getInput("End date(yyyy/mm/dd): ")
        payment = self.getInput("Payment")

    def getInput(self, prompt=""):
        return input(prompt)