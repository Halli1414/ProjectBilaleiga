from RepositoryLayer.OrderRepository import OrderRepository
# This is the OrderService class

class OrderService(object):

    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__orders = self.__order_repo.getOrders()

    def addOrder(self, order):
        self.__order_repo.addOrder(order)

    def getOrders(self):
        return self.__order_repo.getOrders()

    def findOrder(slef, order_id):
        return_order = None
        for order in self.__orders:
            if order.getID = order_id:
                return_order = order
        return return_order