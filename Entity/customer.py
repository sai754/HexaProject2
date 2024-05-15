class Customer:
    def __init__(self,firstname,lastname,email,phonenumber,address,username,password,registrationdate):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__phonenumber = phonenumber
        self.__address = address
        self.__username = username
        self.__password = password
        self.__registrationdate = registrationdate

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_email(self):
        return self.__email

    def get_phonenumber(self):
        return self.__phonenumber

    def get_address(self):
        return self.__address

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_registrationdate(self):
        return self.__registrationdate

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def set_email(self, email):
        self.__email = email

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def set_address(self, address):
        self.__address = address

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_registrationdate(self, registrationdate):
        self.__registrationdate = registrationdate
    
    def Authenticate(self,password):
        return self.__password == password
