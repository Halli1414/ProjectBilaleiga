class Order(object):

    def __init__(self, id, customer, vehicle, order_start_date, order_end_date):
        self.__id = id
        self.__customer = customer
        self.__vehicle = vehicle
        self.__order_start = order_start_date
        self.__order_end = order_end_date

    def getID(self):
        return self.__id

    def getCustomer(self):
        return self.__customer
    
    def getVehicle(self):
        return self.__vehicle

    def getOrderStartDate(self):
        return self.__order_start

    def getOrderEndDate(self):
        return self.__order_end

    def setCustomer(self, new_customer):
        self.__customer = new_customer

    def setVehicle(self, new_Vehicle):
        self.__vehicle = new_Vehicle

    def setOrderStartDate(self, new_start_date):
        self.__order_start = new_start_date

    def setOrderEndDate(self, new_end_date):
        self.__order_end = new_end_date