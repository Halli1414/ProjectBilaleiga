from Models.Order import Order
from Models.Customer import Customer
from Models.Vehicle import Vehicle
# This is the OrderRepository class

class OrderRepository(object):

    def __init__(self):
        self.__orders = []

    def addOrder(self, order):

        self.__orders.append(order)

        with open("./Data/orders.txt", "a+") as order_file:
            order_id = order.getID()
            customer = order.getCustomer()
            vehicle = order.getVehicle()
            order_start_date = order.getOrderStartDate()
            order_end_date = order.getOrderEndDate()
            order_file.write("{},{},{},{},{}\n".format(
                order_id, customer, vehicle, order_start_date, order_end_date
                ))

    def getOrders(self):
        if self.__orders == []:
            self.refreshOrderList()
        return self.__orders

    def updateOrderFile(self, order_list):
        str_with_orders = ""
        with open("./Data/orders.txt", "w") as order_file:
            for order in order_list:
                order_id = order.getID()
                customer = order.getCustomer()
                vehicle = order.getVehicle()
                order_start_date = order.getOrderStartDate()
                order_end_date = order.getOrderEndDate()
                str_with_orders += "{},{},{},{},{}\n".format(
                order_id, customer, vehicle, order_start_date, order_end_date
                )
            order_file.write(str_with_orders)
        self.refreshOrderList()

    def customerToOject(self, customer_str):
        name, customer_id, email, phone, address = customer_str.split(";")
        a_customer = Customer(name, customer_id, email, phone, address)
        return a_customer

    def vehicleToObject(self, vehicle_str):
        manufacturer, model, vehicle_id, color, kilometers,  vehicle_status, category = vehicle_str.split(";")
        a_vehicle = Vehicle(manufacturer, model, vehicle_id, color, kilometers, vehicle_status, category,)
        return a_vehicle

    def refreshOrderList(self):
        self.__orders = []
        with open("./Data/orders.txt", "r") as order_file:
            for line in order_file.readlines():
                line = line.strip("\n")
                order_id, customer, vehicle, order_start_date, order_end_date = line.split(",")
                customer_obj = self.customerToOject(customer)
                vehicle_obj = self.vehicleToObject(vehicle)
                new_order = Order(
                    order_id, customer_obj, vehicle_obj, order_start_date, order_end_date
                )
                self.__orders.append(new_order)
