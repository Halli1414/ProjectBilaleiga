from Models.Order import Order
from Models.Customer import Customer
from Models.Vehicle import Vehicle
# This is the OrderRepository class

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

    def getOrders(self):
        if self.__orders == []:
            with open("./Data/orders.txt", "r") as order_file:
                for line in order_file.readlines():
                    order_id, customer, vehicle, order_start_date, order_end_date, payment = line.split(",")
                    customer_obj = self.customerToOject(customer)
                    vehicle_obj = self.vehicleToObject(vehicle)
                    new_order = Order(
                        order_id, customer_obj, vehicle_obj, order_start_date, order_end_date, payment
                    )
                    self.__orders.append(new_order)
        return self.__orders

    def customerToOject(self, customer_str):
        name, customer_id, email, phone, address = customer_str.split(";")
        a_customer = Customer(name, customer_id, email, phone, address)
        return a_customer

    def vehicleToObject(self, vehicle_str):
        manufacturer, model, vehicle_id, color, kilometers,  vehicle_status, category = vehicle_str.split(";")
        a_vehicle = Vehicle(manufacturer, model, vehicle_id, color, kilometers, vehicle_status, category,)
        return a_vehicle