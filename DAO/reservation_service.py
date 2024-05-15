from Util.DBConn import DBConnection
class ReservationService(DBConnection):
    def __init__(self,custservice,vehiserv):
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
        return self.cursor.fetchall()
    def CreateReservation(self,reserv):
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
        elif updater == "Admin":
            self.cursor.execute("""
                           update Reservation
                           set CustomerID = ?, VehicleID = ?, StartDate = ?, EndDate = ?, TotalCost = ?, Status = ?
                           where ReservationID = ?""",
                           (reservation.get_customerid(),reservation.get_vehicleid(),reservation.get_startdate(),reservation.get_enddate(),
                            reservation.get_totalcost(),
                            reservation.get_status(),reservid))
            self.conn.commit()
            print("Reservation Updated Successfully")
    
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