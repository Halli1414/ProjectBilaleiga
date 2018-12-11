from ServiceLayer.CustomerService import CustomerService
from Models.Customer import Customer

class CustomerUI:

    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__choice = ""

    def start(self):
        while coice != "q":
            self._PrintMenu
            self._NewCustomer
            self._FindCustomer
            self._AllCustomer

    def PrintMenu(self):
        print("1. New Customer ")
        print("2. Find Customer ")
        print("3. All customer ")
        print("4. Update customer ")
        print("5. Delete customer ")
   
    def NewCustomer(self):
        name = input("Name: ")
        customer_id = input("ID: ")
        email = input("Email: ")
        phone = input("Phone number: ")
        address = input("Address: ")

        NewCustomer = Customer(name, customer_id, phone, address, email)
        self.__CustomerService.AddCustomer(NewCustomer)
    
    def FindCustomer(self):
        customer_id = input("ID: ")

        self.__CustomerService.FindCustomer(customer_id)

    def AllCustomer(self):
        customers = self.__CustomerService.GetCustomer()
  
