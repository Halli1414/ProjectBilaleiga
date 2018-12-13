from RepositoryLayer.OrderRepository import OrderRepository
from Models.Order import Order
# This is the OrderService class

class OrderService(object):

    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__orders = self.__order_repo.getOrders()

    def addOrder(self, order):
        self.__order_repo.addOrder(order)

    def getOrders(self):
        return self.__order_repo.getOrders()

    def getLastOrderID(self):
        if self.__orders == []:
            return 0
        else:
            return self.__orders[-1].getID()

    def findOrder(self, selected_order):
        return_order = None
        for order in self.__orders:
            if order.getID() == selected_order.getID():
                return_order = order
        return return_order

    def updateOrder(
        self, order_id, customer, vehicle, start_date, end_date, payment=""
        ):

        for order in self.__orders:
            if order.getID() == order_id:
                order.setCustomer(customer)
                order.setVeicle(vehicle)
                order.setOrderStartDate(start_date)
                order.setOrderEndDate(end_date)
                order.setPayment(payment)

                return "Order successfully updated"
    def deleteOrder(self, selected_order):
        for i in range(0, len(self.__orders)):
            if self.__orders[i].getID() == selected_order.getID():
                self.__orders.pop(i)
                return "Order deleted"
            else:
                return "Order not found"