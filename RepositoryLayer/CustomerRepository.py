# This is the CustomerRepository class
from Models.Customer import Customer

class CustomerRepository:
    
    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        with open("/data/customer.txt","a+") as customer_file:
            name = customer.get_name()
            id = customer.get_id()
            phone = customer.get_phone()
            address = customer.get_address()
            email = customer.get_email()
            customer_file.write("{},{},{},{},{}\n".format(name, id, phone, address, email))
    
    def get_customer(self):
        if self.__customer == []:
            with open("./data/customer.txt", "r") as customer_file:
                for line in customer_file.readlines():
                    name, id, phone, address, email = line.split(",")
                    new_customer = Customer(name, id, phone, address, email)
                    self.__customer.append(new_customer)
        
        return self.__customer