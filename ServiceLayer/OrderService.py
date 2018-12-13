from RepositoryLayer.OrderRepository import OrderRepository
from Models.Order import Order
# This is the OrderService class

class OrderService(object):

    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__orders = self.__order_repo.getOrders()

    def getLastOrderID(self):
        if self.__orders == []:
            return 0
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
        self.refresh_orders_list()
        return new_order

    def getOrders(self):
        return self.__order_repo.getOrders()



    def findOrder(self, order_id):
        return_order = None
        for order in self.__orders:
            if order.getID() == order_id:
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

    def refresh_orders_list(self):
        self.__orders = self.__order_repo.getOrders()