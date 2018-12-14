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
        phone = input("Phone number: ")
        address = input("Address: ")
        email = input("Email: ")

        new_customer = Customer(name, customer_id, phone, address, email)
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

    def updateCustomer(self, selected_customer):
        # Initialize values
        customer_id = selected_customer.getID()
        attr_list = []
        attr_list[0] = selected_customer.getName()
        attr_list[1] = selected_customer.getEmail()
        attr_list[2] = selected_customer.getPhone()
        attr_list[3] = selected_customer.getAddress()

        for attr in attr_list:
            self.selectNewAttr(attr)

        new_name = attr_list[0]
        new_email = attr_list[1]
        new_phone = attr_list[2]
        new_address = attr_list[3]

        self.__customer_service.updateCustomer(
            customer_id, new_name, new_phone, new_address, new_email
            )
        
    def deleteCustomer(self):
       self.__customer_service.deleteCustomer(self.__selected_customer)

    


    def confirmUpdatedAttr(self, customer_attr):
        print(customer_attr)
        print("Use this?(Y/N)")
        
        return self.getInput().lower()

    def selectNewAttr(self, customer_attr):
        new_attr = customer_attr
        choice = self.confirmUpdatedAttr(new_attr)
        while choice != "y":
            new_attr = self.getInput("New name: ")
            choice = self.confirmUpdatedAttr(new_attr)

        return new_attr
        

    def getInput(self, prompt=""):
        return input(prompt)