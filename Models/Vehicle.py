
class Vehicle:
    def __init__(
        self, manufacturer, model, id, color, kilometers,  vehicle_status, category
        ):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__id = id
        self.__color = color
        self.__kilometers = kilometers
        self.__vehicle_status = vehicle_status
        self.__category = category
    
    def getID(self):
        return self.__id
    def getManufacturer(self):
        return self.__manufacturer
    def getModel(self):
        return self.__model
    def getColor(self):
        return self.__color
    def getKilometers(self):
        return self.__kilometers
    def getCategory(self):
        return self.__category
    def getVehicleStatus(self):
        return self.__vehicle_status
    def setKilometers(self, new_Kilometers):
        self.__kilometers = new_Kilometers
    def setVehicleStatus(self, new_VehicleStatus):
        self.__vehicle_status = new_VehicleStatus
    def setCategory(self, new_Category):
        self.__category = new_Category
    
    def __str__(self):
        return "{};{};{};{};{};{};{}".format(
            self.__id, self.__manufacturer, self.__model, self.__color, self.__kilometers, self.__vehicle_status, self.__category
        )
    


