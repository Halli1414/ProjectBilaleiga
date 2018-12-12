
class Vehicle:
    def __init__(
        self, manufacturer, model, id, color, kilometers,  vehicleStatus, category
        ):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__id = id
        self.__color = color
        self.__kilometers = kilometers
        self.__vehicleStatus = vehicleStatus
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
    def setKilometers(self):
        return self.__kilometers
    def setVehicleStatus(self):
        return self.__vehicleStatus
    def setCategory(self):
        return self.__category
    
    def __str__(self):
        return "Order ID: {} Manufacturer: {} Model: {} Color: {} Kilometers: {} VehicleStatus {}".format(
            self.__id, self.__manufacturer, self.__model, self.__color, self.__kilometers, self.__vehicleStatus
        )
    


