# This is the CustomerService class

from RepositoryLayer.CustomerRepository import CustomerRepository

class CostumerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def addCustomer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)
    
    def isValidCustomer(self, customer):
        #Setja inn kóða
        return True
    
    def getCustomer(self):
        return self.__customer_repo.get_customer()
    
    