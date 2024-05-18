from abc import ABC,abstractmethod
class ICustomerService(ABC):
    @abstractmethod
    def GetCustomerByID(customerid):
        pass
    @abstractmethod
    def GetCustomerByUsername(username):
        pass
    @abstractmethod
    def RegisterCustomer(newCustomer):
        pass
    @abstractmethod
    def UpdateCustomer(customer, name):
        pass
    @abstractmethod
    def DeleteCustomer(customerID):
        pass