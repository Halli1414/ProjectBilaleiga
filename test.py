from Models.Order import Order
from Models.Customer import Customer
from Models.Vehicle import Vehicle
from datetime import datetime

class OrderRepository(object):

    def __init__(self):
        self.__orders = []
    
    def addOrder(self, order):
        with open("./Data/orders.txt", "a+") as order_file:
            order_id = order.getID()
            customer = order.getCustomer()
            vehicle = order.getVehicle()
            order_start_date = order.getOrderStartDate()
            order_end_date = order.getOrderEndDate()
            payment = order.getPayment()
            order_file.write("{},{},{},{},{},{}\n".format(
                order_id, customer, vehicle, order_start_date, order_end_date, payment
                ))


customer = Customer("Guy", "1212343456","1234567", "None", "mail@mail.is")
vehicle = Vehicle("Nissan", "Micra", "DB583", "black", 156000, "1", "1")
order = Order(7,customer,vehicle,datetime(2018, 12, 12).date(), datetime(2018,12,30).date(), "yes" )
test_repo = OrderRepository()
test_repo.addOrder(order)
