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
    
    def getCustomer(self):
        return self.__customer_repo.getCustomer()

    def findCustomer(self, customer_id):

        for customer in self.__customers:
            if customer.getID() == customer_id:
                return customer
    
    def deleteCustomer(self, selected_customer):
        for i in range(0,len(self.__customers)):
            if self.__customers[i].getID() == selected_customer.getID():
                self.__customers.pop(i)
                self.__customer_repo.deleteCustomer(self.__customers)
    
    def updateCustomer(self, a_customer, name, phone, address, email):
        for customer in self.__customers:
            if customer.getID() == a_customer.getID():
                customer.setName(name)
                customer.setPhone(phone)
                customer.setAddress(address)
                customer.setEmail(email)
