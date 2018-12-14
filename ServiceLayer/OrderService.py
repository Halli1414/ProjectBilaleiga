from RepositoryLayer.OrderRepository import OrderRepository
from Models.Order import Order
# This is the OrderService class

class OrderService(object):

    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__orders = self.__order_repo.getOrders()

    def getLastOrderID(self):
        # Get the lates list
        self.getOrders()

        # Check if list is empty
        if self.__orders == []:
            return 0
        # Return the last elements ID
        else:
            return self.__orders[-1].getID()

    def getNextOrderID(self):
        next_id = int(self.getLastOrderID())
        next_id += 1
        return str(next_id)

    def addOrder(self, customer, vehicle, start_date, end_date):

        order_id = self.getNextOrderID()

        new_order = Order(order_id, customer, vehicle, start_date, end_date)
        self.__order_repo.addOrder(new_order)
        self.getOrders()
        return new_order

    def getOrders(self):
        self.__orders =  self.__order_repo.getOrders()
        return self.__orders



    def findOrder(self, order_id):
        return_order = None
        for order in self.__orders:
            if order.getID() == order_id:
                return_order = order
        return return_order

    def updateOrder(
        self, order_id, customer, vehicle, start_date, end_date
        ):

        self.getOrders()

        for order in self.__orders:
            if order.getID() == order_id:
                order.setCustomer(customer)
                order.setVehicle(vehicle)
                order.setOrderStartDate(start_date)
                order.setOrderEndDate(end_date)

                self.__order_repo.updateOrderFile(self.__orders)
                self.getOrders()
                return "Order: {} successfully updated".format(order_id)

        return "Order ID: {} not found".format(order_id)

    def deleteOrder(self, selected_order_id):
        self.getOrders()
        for i in range(0, len(self.__orders)):
            if self.__orders[i].getID() == selected_order_id:
                self.__orders.pop(i)
                self.__order_repo.updateOrderFile(self.__orders)
                return "Order ID: {} deleted".format(selected_order_id)
        
        return "Order ID: {} not found".format(selected_order_id)