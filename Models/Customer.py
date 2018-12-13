class Customer():
    def __init__(self, name, customer_id, phone, address, email):
        self.__name = name
        self.__id = customer_id
        self.__phone = phone
        self.__address = address
        self.__email = email
    
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getPhone(self):
        return self.__phone
    
    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

    def setName(self, new_name):
        self.__name = new_name
    
    def setPhone(self, new_phone):
        self.__phone = new_phone

    def setAddress(self, new_address):
        self.__address = new_address
    
    def setEmail(self, new_email):
        self.__email = new_email

    def __str__(self):
        return "{};{};{};{};{}".format(self.__name, self.__id, self.__phone, self.__address, self.__email)
