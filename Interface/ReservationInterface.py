from abc import ABC, abstractmethod
class IReservationService(ABC):
    @abstractmethod
    def GetReservationByID(reservationid):
        pass
    @abstractmethod
    def GetReservationByCustomerID(customerid):
        pass
    @abstractmethod
    def CreateReservation(reservation):
        pass
    @abstractmethod
    def UpdateReservation(reservation,reservid,updater):
        pass
    @abstractmethod
    def CancelReservation(reservationid):
        pass