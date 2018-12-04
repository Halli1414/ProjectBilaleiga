class PaymentInfo:
    def __init__(self, card_number, card_company, amount):
        self.__card_number = card_number
        self.__card_company = card_company
        self.__amount = amount

    def __str__(self):
        return "Card number: {}, Card company: {}, Amount: {}".format(self.__card_number, self.__card_company, self.__amount)
    
    def getCardNumber(self):
        return self.__card_number

    def getCardCompany(self):
        return self.__card_company

    def getAmount(self):
        return self.__amount
    
    def setAmount(self, new_amount):
        self.__amount = new_amount