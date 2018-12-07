from ServiceLayer.CustomerService import CustomerService
from Models.Customer import Customer

class CustomerUI:

    def __init__(self):
        self.__customer_service = CustomerService()

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

        new_customer = Customer(name, customer_id, phone, address, email)
        self.__customer_service.addCustomer(new_customer)

    def DeleteCustomer(self):


