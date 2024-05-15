class Vehicle:
    def __init__(self,model,make,year,color,registrationnumber,availability,dailyrate):
        self.__model = model
        self.__make = make
        self.__year = year
        self.__color = color
        self.__registrationnumber = registrationnumber
        self.__availability = availability
        self.__dailyrate = dailyrate
    
    def get_model(self):
        return self.__model

    def get_make(self):
        return self.__make

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_registrationnumber(self):
        return self.__registrationnumber

    def get_availability(self):
        return self.__availability

    def get_dailyrate(self):
        return self.__dailyrate

    def set_model(self, model):
        self.__model = model

    def set_make(self, make):
        self.__make = make

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color

    def set_registrationnumber(self, registrationnumber):
        self.__registrationnumber = registrationnumber

    def set_availability(self, availability):
        self.__availability = availability

    def set_dailyrate(self, dailyrate):
        self.__dailyrate = dailyrate