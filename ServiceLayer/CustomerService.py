# This is the CustomerService class

from RepositoryLayer.CustomerRepository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def AddCustomer(self, customer):
        if self.IsValidCustomer(customer):
            self.__customer_repo.AddCustomer(customer)
    
    def IsValidCustomer(self, customer):
        #Setja inn kóða
        return True
    
    def GetCustomer(self):
        return self.__customer_repo.GetCustomer()
    
    