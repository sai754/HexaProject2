from abc import ABC, abstractmethod
class IVehicleService(ABC):
    @abstractmethod
    def GetVehicleByID(vehicleid):
        pass
    @abstractmethod
    def GetAvailableVehicle():
        pass
    @abstractmethod
    def AddVehicle(vehicle):
        pass
    @abstractmethod
    def UpdateVehicle(vehicle,vehicleid):
        pass
    @abstractmethod
    def RemoveVehicle(vehicleid):
        pass