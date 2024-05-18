from abc import ABC, abstractmethod
class IAdminService(ABC):
    @abstractmethod
    def GetAdminById(adminId):
        pass
    @abstractmethod
    def GetAdminByUsername(username):
        pass
    @abstractmethod
    def RegisterAdmin(adminData):
        pass
    @abstractmethod
    def UpdateAdmin(adminData,adminName):
        pass
    @abstractmethod
    def DeleteAdmin(adminName):
        pass