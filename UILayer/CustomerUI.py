from ServiceLayer.CustomerService import CustomerService
from Models.Customer import Customer

class CustomerUI:

    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__choice = ""

    def start(self):
        while self.__choice != "q":
            self.PrintMenu()
            self.__choice = input("")
            if self.__choice == "1":
                self.NewCustomer()
            elif self.__choice == "2": 
                self.FindCustomer()
            elif self.__choice == "3":
                self.AllCustomer()
            elif self.__choice == "4":
                self.UpdateCustomer()
            elif self.__choice == "5":
                self.DeleteCustomer()

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

        customer = self.__CustomerService.FindCustomer(customer_id)
        print(customer)

    def AllCustomer(self):
        customers = self.__CustomerService.GetCustomer()
  
    def UpdateCustomer(self):
        name = input("Name: ")
        customer_id = input("ID: ")
        email = input("Email: ")
        phone = input("Phone number: ")
        address = input("Address: ")

    def DeleteCustomer(self):
        pass