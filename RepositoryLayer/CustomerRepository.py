# This is the CustomerRepository class
from models.Costumer import Costumer

class CostumerRepository:
    
    def __init__(self):
        self.__costumer = []

    def add_costumer(self, costumer):
        with open("/data/costumer.txt","a+") as costumer_file:
            name = costumer.get_name()
            id = costumer.get_id()
            phone = costumer.get_phone()
            address = address.get_address()
            email = email.get_email()
            costumer_file.write("{},{},{},{},{}\n".format(name, id, phone, address, email))
    
    def get_costumer(self):
        if self.__costumer == []:
            with open("./data/costumer.txt", "r") as costumer_file:
                for line in costumer_file.readlines():
                    name, id, phone, address, email = line.split(",")
                    new_costumer = costumer(name, id, phone, address, email)
                    self.__costumer.append(new_costumer)
        
        return self.__costumer