# This is the CustomerRepository class
from Models.Customer import Customer

class CustomerRepository:
    
    def __init__(self):
        self.__customers = []

    def addCustomer(self, customer):

        self.__customers.append(customer)

        with open("./Data/customer.txt","a+") as customer_file:
            name = customer.getName()
            customer_id = customer.getID()
            phone = customer.getPhone()
            address = customer.getAddress()
            email = customer.getEmail()
            customer_file.write("{},{},{},{},{}\n".format(name, customer_id, phone, address, email))
    
    def getCustomer(self):
        if self.__customers == []:
            self.refreshCustomerList()
        return self.__customers
    
    def clearCustomerFile(self):
        with open("./Data/customer.txt","w") as customer_file:
            customer_file.write("")

    def deleteCustomer(self, customers):
        self.clearCustomerFile()
        with open("./Data/customer.txt","a+") as customer_file:
            for customer in customer_file:
                name = customer.getName()
                customer_id = customer.getID()
                phone = customer.getPhone()
                address = customer.getAddress()
                email = customer.getEmail()
                customer_file.write("{},{},{},{},{}\n".format(name, customer_id, phone, address, email))
    
    def updateCustomerFile(self, customer_list):
        str_with_customers = ""
        with open("./Data/customer.txt","w") as customer_file:
            for customer in customer_list:
                name = customer.getName()
                customer_id = customer.getID()
                phone = customer.getPhone()
                address = customer.getAddress()
                email = customer.getEmail()
                str_with_customers += "{},{},{},{},{}\n".format(
                    name, customer_id, phone, address, email
                ) 
            customer_file.write(str_with_customers)

    def refreshCustomerList(self):
        self.__customers = []
        with open("./Data/customer.txt", "r") as customer_file:
            for line in customer_file.readlines():
                line = line.strip("\n")
                name, customer_id, phone, address, email = line.split(",")
                new_customer = Customer(name, customer_id, phone, address, email)
                self.__customers.append(new_customer)