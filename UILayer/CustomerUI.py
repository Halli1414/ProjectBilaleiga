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
        self.__selected_customer = customer
        return customer

    def allCustomers(self):
        customers = self.__customer_service.getCustomers()
        self.printCustomerResaults(customers)

    def updateCustomer(self, selected_customer):
        # Initialize values
        customer_id = selected_customer.getID()
        attr_list = []
        attr_list.append(selected_customer.getName())
        attr_list.append(selected_customer.getEmail())
        attr_list.append(selected_customer.getPhone())
        attr_list.append(selected_customer.getAddress())

        for i in range(0, len(attr_list)):
            attr_list[i] = self.selectNewAttr(attr_list[i])

        new_name = attr_list[0]
        new_email = attr_list[1]
        new_phone = attr_list[2]
        new_address = attr_list[3]

        message = self.__customer_service.updateCustomer(
            customer_id, new_name, new_phone, new_address, new_email
            )
        
        print(message)

    def deleteCustomer(self):
       self.__customer_service.deleteCustomer(self.__selected_customer.getID())

    


    def confirmUpdatedAttr(self, customer_attr):
        print(customer_attr)
        print("Use this?(Y/N)")
        
        return self.getInput().lower()

    def selectNewAttr(self, customer_attr):
        new_attr = customer_attr
        choice = self.confirmUpdatedAttr(new_attr)
        while choice != "y":
            new_attr = self.getInput("New: ")
            choice = self.confirmUpdatedAttr(new_attr)

        return new_attr
        

    def getInput(self, prompt=""):
        return input(prompt)

    def printHeader(self):
        print("{:<5}{:<30} {:<20} {:<15} {:<30} {:<25}\n".format(
            "NO.","Name", "ID", "Phone", "Address", "Email"
            ))

    def printCustomerList(self, a_list):
        self.printHeader()
        for i in range(1, len(a_list) + 1):
            customer_str = self.printCustomer(a_list[i-1])
            print("{:>3}. {}".format(i, customer_str))

    def printCustomer(self, customer):
        return "{:.<30} {:.<20} {:.<15} {:.<30} {:<25}".format(
            customer.getName(), customer.getID(), customer.getPhone(),
            customer.getAddress(), customer.getEmail()
            )

    def printCustomerResaults(self, resaults):
        resaults_list = []
        if type(resaults) == list:
            resaults_list = resaults
        elif type(resaults) == Customer:
            resaults_list.append(resaults)
        self.printCustomerList(resaults_list)

