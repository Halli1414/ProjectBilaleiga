# This is the CustomerRepository class
from Models.Customer import Customer

class CustomerRepository:
    
    def __init__(self):
        self.__customer = []

    def AddCustomer(self, customer):
        with open("./Data/customer.txt","a+") as customer_file:
            name = customer.getName()
            customer_id = customer.getID()
            phone = customer.getPhone()
            address = customer.getAddress()
            email = customer.getEmail()
            customer_file.write("{},{},{},{},{}\n".format(name, customer_id, phone, address, email))
    
    def GetCustomer(self):
        if self.__customer == []:
            with open("./Data/customer.txt", "r") as customer_file:
                for line in customer_file.readlines():
                    name, customer_id, phone, address, email = line.split(",")
                    new_customer = Customer(name, customer_id, phone, address, email)
                    self.__customer.append(new_customer)
        
        return self.__customer