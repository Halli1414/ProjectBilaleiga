#this is the ui class that handles all of the menus
class MainMenu:
    def __init__(self, vehicle_service, customer_service, order_service):
        self.__vehicle_service = vehicle_service
        self.__customer_service = customer_service
        self.__order_service = order_service


    def getInput(self):
        return input

    def printScreen(self):
       # return Menu????