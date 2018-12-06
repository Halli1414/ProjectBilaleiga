from Models.Order import Order
# This is the OrderRepository class

class OrderRepository(object):

    def __init__(self):
        self.__orders = []

    def add_order(self, order):
        with open("./data/orders.txt" "a+") as order_file:
            order_id = order.getID()
            customer = order.getCustomer()
            vehicle = order.getVehicle()
            order_start_date = order.getOrderStartDate()
            order_end_date = order.getOrderEndDate()
            payment = order.getPayment()
            order_file.write("{},{},{},{},{},{}\n".format(
                order_id, customer, vehicle, order_start_date, order_end_date, payment
                ))

    def get_orders(self):
        if self.__orders == []:
            with open("./data/orders.txt", "r") as order_file:
                for line in order_file.readlines():
                    order_id, customer, vehicle, order_start_date, order_end_date, payment = line.split(",")
                    new_order = Order(
                        order_id, customer, vehicle, order_start_date, order_end_date, payment
                    )
                    self.__orders.append(new_order)
        return self.__orders
