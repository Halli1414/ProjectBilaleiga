# This is the CustomerService class

from RepositoryLayer.CustomerRepository import CustomerRepository
from Models.Customer import Customer

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()
        self.__customers = self.__customer_repo.getCustomer()

    def addCustomer(self, customer):
        if self.isValidCustomer(customer):
            self.__customer_repo.addCustomer(customer)
    
    def isValidCustomer(self, customer):
        #Setja inn kóða
        return True
    
    def getCustomers(self):
        self.__customers = self.__customer_repo.getCustomer()
        return self.__customers

    def findCustomer(self, customer_id):

        for customer in self.__customers:
            if customer.getID() == customer_id:
                return customer
    
    def deleteCustomer(self, customer_id):
        self.getCustomers()
        for i in range(0,len(self.__customers)):
            if self.__customers[i].getID() == customer_id:
                self.__customers.pop(i)
                self.__customer_repo.updateCustomerFile(self.__customers)
    
    def updateCustomer(self, customer_id, name, phone, address, email):
        self.getCustomers()
        for customer in self.__customers:
            if customer.getID() == customer_id:
                customer.setName(name)
                customer.setPhone(phone)
                customer.setAddress(address)
                customer.setEmail(email)
                self.__customer_repo.updateCustomerFile(self.__customers)
                self.getCustomers()
                return "Customer ID: {} successfully updated".format(
                    customer_id
                    )
        return "Customer ID: {} not found".format(customer_id)
