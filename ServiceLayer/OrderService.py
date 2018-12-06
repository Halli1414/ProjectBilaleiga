from RepositoryLayer.OrderRepository import OrderRepository
# This is the OrderService class

class OrderService(object):

    def __init__(self):
        self.__order_repo = OrderRepository()

    def addOrder(self, order):
        self.__order_repo.addOrder(order)

    def getOrders(self):
        return self.__order_repo.getOrders()