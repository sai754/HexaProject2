from Util.DBConn import DBConnection
from tabulate import tabulate
from abc import ABC, abstractmethod
from Exceptions.exceptions import VehicleNotFoundException

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
class VehicleService(DBConnection, IVehicleService):
    def GetVehicle(self):
        self.cursor.execute("Select * from Vehicle")
        vehicles = self.cursor.fetchall()
        headers = [column[0] for column in self.cursor.description]
        print(tabulate(vehicles,headers=headers,tablefmt="psql"))
    def GetVehicleByID(self,id):
        self.cursor.execute("Select * from Vehicle where VehicleID = ?",(id))
        vehicle = self.cursor.fetchone()
        return vehicle
    def GetAvailableVehicle(self):
        self.cursor.execute("Select * from Vehicle where Availability = 1")
        vehicles = self.cursor.fetchall()
        headers = [column[0] for column in self.cursor.description]
        print(tabulate(vehicles,headers=headers,tablefmt="psql"))
    def AddVehicle(self,vehicle):
        self.cursor.execute("insert into Vehicle values (?,?,?,?,?,?,?)",
                       (vehicle.get_model(), vehicle.get_make(), vehicle.get_year(),
                        vehicle.get_color(), vehicle.get_registrationnumber(),
                        vehicle.get_availability(), vehicle.get_dailyrate()))
        self.conn.commit()
        print("Added Successfully")
    
    def UpdateVehicle(self,vehicle,vehicleid):
        try:
            self.cursor.execute("""
                        update vehicle
                        set Model = ?, Make = ?, Year = ?, Color = ?, RegistrationNumber = ?, Availability = ?, DailyRate = ?
                        where VehicleID = ?""",
                        (vehicle.get_model(), vehicle.get_make(), vehicle.get_year(),
                            vehicle.get_color(), vehicle.get_registrationnumber(),
                            vehicle.get_availability(), vehicle.get_dailyrate(),vehicleid))
            self.conn.commit()
            print("Updated Successfully")
        except VehicleNotFoundException as e:
            print(e)
    
    def RemoveVehicle(self,id):
        self.cursor.execute("delete from Vehicle where VehicleID = ?",(id))
        self.conn.commit()
        print("Deleted Successfully")
    
    def GetAllVehicles(self):
        self.cursor.execute("select * from Vehicle")
        vehicles =  self.cursor.fetchall()
        headers = [column[0] for column in self.cursor.description]
        return vehicles, headers
