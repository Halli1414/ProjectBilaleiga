from Models.Order import Order
from Models.Customer import Customer
from Models.Vehicle import Vehicle
from datetime import datetime
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
            order_fee = order.getOrderFee()
            order_file.write("{},{},{},{},{},{}\n".format(
                order_id, customer, vehicle, order_start_date, order_end_date, order_fee
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
                order_fee = order.getOrderFee()
                str_with_orders += "{},{},{},{},{},{}\n".format(
                order_id, customer, vehicle, order_start_date, order_end_date, order_fee
                )
            order_file.write(str_with_orders)
        self.refreshOrderList()

    def customerToObject(self, customer_str):
        name, customer_id, email, phone, address = customer_str.split(";")
        a_customer = Customer(name, customer_id, email, phone, address)
        return a_customer

    def vehicleToObject(self, vehicle_str):
        manufacturer, model, vehicle_id, color, kilometers,  vehicle_status, category = vehicle_str.split(";")
        a_vehicle = Vehicle(manufacturer, model, vehicle_id, color, kilometers, vehicle_status, category,)
        return a_vehicle

    def __dateToObject(self, date):
        year, month, day = date.split("-")
        date_obj = datetime(int(year), int(month), int(day)).date()
        return date_obj

    def refreshOrderList(self):
        self.__orders = []
        with open("./Data/orders.txt", "r") as order_file:
            for line in order_file.readlines():
                line = line.strip("\n")
                order_id, customer, vehicle, order_start_date, order_end_date, order_fee = line.split(",")
                customer_obj = self.customerToObject(customer)
                vehicle_obj = self.vehicleToObject(vehicle)
                start_date_obj = self.__dateToObject(order_start_date)
                end_date_obj = self.__dateToObject(order_end_date)
                new_order = Order(
                    order_id, customer_obj, vehicle_obj, start_date_obj, end_date_obj, int(order_fee)
                )
                self.__orders.append(new_order)
