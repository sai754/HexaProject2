from Exceptions.exceptions import AuthenticationException
class Admin:
    def __init__(self,firstname,lastname,email,phonenumber,username,password,role,joindate):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__phonenumber = phonenumber
        self.__username = username
        self.__password = password
        self.__role = role
        self.__joindate = joindate

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_email(self):
        return self.__email

    def get_phonenumber(self):
        return self.__phonenumber

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role

    def get_joindate(self):
        return self.__joindate

    def set_firstname(self, firstname):
        self.__firstname = firstname
    
    def set_lastname(self, lastname):
        self.__lastname = lastname
    
    def set_email(self, email):
        self.__email = email
    
    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber
    
    def set_username(self, username):
        self.__username = username
    
    def set_password(self, password):
        self.__password = password
    
    def set_role(self, role):
        self.__role = role
    
    def set_joindate(self, joindate):
        self.__joindate = joindate
    
    def Authenticate(self,password):
        try:
            return self.__password == password
        except AuthenticationException as e:
            print(e)
    