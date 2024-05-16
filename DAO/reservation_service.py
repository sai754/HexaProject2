from Util.DBConn import DBConnection
from abc import ABC, abstractmethod
from Exceptions.exceptions import ReservationException
from tabulate import tabulate

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
class ReservationService(DBConnection, IReservationService):
    def __init__(self,custservice,vehiserv):
        super().__init__()
        self.custservice = custservice
        self.vehiserv = vehiserv
    
    def GetReservationByID(self,reservID):
        self.cursor.execute("Select * from Reservation where ReservationID = ?",(reservID))
        return self.cursor.fetchone()
    
    def GetReservationByCustomerID(self,custid):
        self.cursor.execute("Select * from Reservation where CustomerID = ?",(custid))
        return self.cursor.fetchall()

    def GetReservationByCustomerName(self,username):
        self.cursor.execute("""Select ReservationID,Reservation.CustomerID,VehicleID, StartDate,EndDate,TotalCost,Status from Reservation join 
                       Customer on Reservation.CustomerID = Customer.CustomerID where Customer.Username = ? """,(username))
        customer = self.cursor.fetchall()
        headers = [column[0] for column in self.cursor.description]
        print(tabulate([customer],headers=headers,tablefmt='psql'))
        return customer
    def CreateReservation(self,reserv):
        try:
            vehicle = self.vehiserv.GetVehicleByID(reserv.get_vehicleid())
            if vehicle and vehicle[6] == True:
                self.cursor.execute("Insert into Reservation Values (?,?,?,?,?,?)",
                            (reserv.get_customerid(),reserv.get_vehicleid(),reserv.get_startdate(),reserv.get_enddate(),
                                reserv.get_totalcost(),reserv.get_status()))
                self.cursor.execute("update Vehicle set Availability = 0 where VehicleID = ?",reserv.get_vehicleid())
                self.conn.commit()
                print("Reservation Created Successfully")
            else:
                print("Vehicle Not Found or unavailable")
                raise ReservationException
        except ReservationException as e:
            print(e)
    def UpdateReservation(self,updater,reservid,reservation):
        if updater == "customer":
            cusomerid = reservation.get_customerid()
            if self.custservice.CheckOwnership(reservid,cusomerid):
                self.cursor.execute("""
                               update Reservation
                               set StartDate = ?, EndDate = ?, TotalCost = ?, Status = ?
                               where ReservationID = ?""",
                               (reservation.get_startdate(),reservation.get_enddate(),
                               reservation.get_totalcost(),reservation.get_status(),reservid))
                self.conn.commit()
                print("Reservation Updated Successfully")
            else:
                print("Your are not authorized to update this reservation")
        # elif updater == "Admin":
        #     self.cursor.execute("""
        #                    update Reservation
        #                    set CustomerID = ?, VehicleID = ?, StartDate = ?, EndDate = ?, TotalCost = ?, Status = ?
        #                    where ReservationID = ?""",
        #                    (reservation.get_customerid(),reservation.get_vehicleid(),reservation.get_startdate(),reservation.get_enddate(),
        #                     reservation.get_totalcost(),
        #                     reservation.get_status(),reservid))
        #     self.conn.commit()
        #     print("Reservation Updated Successfully")
    def UpdateReservationByAdmin(self):
        ReservationService.GetReservations()
        reserveid = int(input("Enter the Reservation Id you want to update: "))
        status = input("Do you want to change the status to (Confirmed) or (Completed): ")
        self.cursor.execute("update Reservation where ReservationID = ? set Status = ?",(reserveid,status))
        print("Updated Successfully")
    
    def CancelReservation(self,reservid):
        reservation = self.GetReservationByID(reservid)
        if reservation:
            self.cursor.execute("delete from Reservation where ReservationID = ?",(reservid))
            self.cursor.execute("update Vehicle set Availability = 1 where VehicleID = ?",(reservation[2]))
            self.conn.commit()
            print("Reservation Deleted Successfully")
        else:
            print("Reservation not found")
    
    def GetReservations(self):
        self.cursor.execute("select * from Reservation")
        reservations = self.cursor.fetchall()
        headers = [column[0] for column in self.cursor.description]
        return reservations, headers