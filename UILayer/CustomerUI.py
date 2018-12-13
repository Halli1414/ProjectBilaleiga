from ServiceLayer.CustomerService import CustomerService
from Models.Customer import Customer

class CustomerUI:

    def __init__(self):
        self.__customer_service = CustomerService()
        self.__choice = ""
        self.__selected_customer = None

    def getSelected(self):
        return self.__selected_customer

    def printMenu(self):
        print("1. New Customer ")
        print("2. Find Customer ")
        print("3. All customer ")
        print("4. Update customer ")
        print("5. Delete customer ")
   
    def newCustomer(self):
        name = input("Name: ")
        customer_id = input("ID: ")
        email = input("Email: ")
        phone = input("Phone number: ")
        address = input("Address: ")

        new_customer = Customer(name, customer_id, email, phone, address)
        self.__customer_service.addCustomer(new_customer)
        self.__selected_customer = new_customer
    
    def findCustomer(self):
        customer_id = input("ID: ")

        customer = self.__customer_service.findCustomer(customer_id)
        print(customer)
        self.__selected_customer = customer

    def allCustomer(self):
        customers = self.__customer_service.getCustomer()
        print("{:<30} {:<20} {:<15} {:<30} {:<25}\n".format(
            "Name", "ID", "Phone", "Address", "Email"))
        for customer in customers:
            print("{:<30} {:<20} {:<15} {:<30} {:<25}".format(customer.getName(), customer.getID(), customer.getPhone(), customer.getAddress(), customer.getEmail()))

    def updateCustomer(self, a_customer):
        name = input("Name: ")
        phone = input("Phone number: ")
        address = input("Address: ")
        email = input("Email: ")
        
        self.__customer_service.updateCustomer(a_customer, name, phone, address,email)
        
    def deleteCustomer(self):
       self.__customer_service.deleteCustomer(self.__selected_customer)

    
