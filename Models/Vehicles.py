
class Vehicles:
    def __init__(
        self, manufacturer, model, id, color, kilometers,  vehicleStatus
        ):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__id = id
        self.__color = color
        self.__kilometers = kilometers
        self.__vehicleStatus = vehicleStatus
    
    def getId(self):
        return self.__id
    def getManufacturer(self):
        return self.__manufacturer
    def getModel(self):
        return self.__model
    def getColor(self):
        return self.__color
    def getKilometers(self):
        return self.__kilometers
    def setKilometers(self):
        return self.__kilometers
    def setVehicleStatus(self):
        return self.__vehicleStatus