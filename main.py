import pyodbc
import datetime 
from tabulate import tabulate

server_name = "DESKTOP-PR637UP"
database_name = "CarConnect"
 
 
conn_str = (
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

print("Database Connected")



# Entity
# Customer Entity

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

# Vehicle Entity
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
        return self.__password == password
    

class Reservation:
    def __init__(self,customerid,vehicleid,startdate,enddate,totalcost,status):
        self.__customerid = customerid
        self.__vehicleid = vehicleid
        self.__startdate = startdate
        self.__enddate = enddate
        self.__totalcost = totalcost
        self.__status = status


    def get_customerid(self):
        return self.__customerid

    def get_vehicleid(self):
        return self.__vehicleid

    def get_startdate(self):
        return self.__startdate

    def get_enddate(self):
        return self.__enddate

    def get_totalcost(self):
        return self.__totalcost

    def get_status(self):
        return self.__status
    
    def set_customerid(self, customerid):
        self.__customerid = customerid

    def set_vehicleid(self, vehicleid):
        self.__vehicleid = vehicleid

    def set_startdate(self, startdate):
        self.__startdate = startdate

    def set_enddate(self, enddate):
        self.__enddate = enddate

    def set_totalcost(self, totalcost):
        self.__totalcost = totalcost

    def set_status(self, status):
        self.__status = status

    
    def CalculateTotalCost(startdate,enddate,dailyrate):
        startdate = datetime.datetime.strptime(startdate,"%Y-%m-%d")
        enddate = datetime.datetime.strptime(enddate,"%Y-%m-%d")
        numdays = (enddate - startdate).days
        totalcost = numdays * dailyrate
        return totalcost

# Service classes
# Authentication Service

class AuthenticationService:
    def __init__(self, service):
        self.service = service
    def authenticate_customer(self, username, password):
        customer_data = self.service.GetCustomerByUsername(username)
        if customer_data:
            customer_obj = Customer(*customer_data[1:])
            return customer_obj.Authenticate(password)
        else:
            print("Customer not found.")
            return False
    def authenticate_admin(self, username, password):
        admin_data = self.service.GetAdminByUsername(username)
        print(admin_data)
        if admin_data:
            admin_obj = Admin(*admin_data[1:])
            return admin_obj.Authenticate(password)
        else:
            print("Admin not found.")
            return False


#Customer Service    
class CustomerService:

    def GetCustomer(self,username):
        cursor.execute("select * from Customer where Username = ?",(username))
        for row in cursor:
            print(row)
    def GetCustomerByID(self,id):
        cursor.execute("Select * from Customer where CustomerID = ?",(id,))
        return cursor.fetchone()

    def GetCustomerByUsername(self,username):
        cursor.execute("Select * from Customer where Username = ?",(username,))
        return cursor.fetchone()

    def RegisterCustomer(self,newCustomer):
        cursor.execute("insert into Customer values (?,?,?,?,?,?,?,?)",
                    (newCustomer.get_firstname(), newCustomer.get_lastname(), newCustomer.get_email(),
                    newCustomer.get_phonenumber(), newCustomer.get_address(), newCustomer.get_username(),
                    newCustomer.get_password(), newCustomer.get_registrationdate()))
        conn.commit()
        print("Registered Successfully")

    def UpdateCustomer(self,customer,customername):
        cursor.execute("""
                    UPDATE Customer
                    SET FirstName = ?, LastName = ?, Email = ?, PhoneNumber = ?, Address = ?, Username = ?, Password = ?
                    WHERE Username = ?
                    """,
                    (customer.get_firstname(), customer.get_lastname(), customer.get_email(),
                     customer.get_phonenumber(), customer.get_address(), customer.get_username(),
                     customer.get_password(),customername))
        conn.commit()
        print("Updated Successfully")

    def DeleteCustomer(self,id):
        cursor.execute("Delete from Reservation where CustomerID = ?",(id))
        cursor.execute("Delete from Customer where CustomerID = ?",(id))
        conn.commit()
        print("Deleted Successfully")

    def CheckOwnership(self, reservation_id, customer_id):
        cursor.execute("SELECT CustomerID FROM Reservation WHERE ReservationID = ?", (reservation_id,))
        fetched_customer_id = cursor.fetchone()[0] 
        return fetched_customer_id == customer_id
    
    def GetCustomerID(self,username):
        cursor.execute("Select CustomerID from Customer where Username = ?",(username))
        custid = cursor.fetchone()[0]
        return custid

# Vehicle Service
class VehicleService:
    def GetVehicle(self):
        cursor.execute("Select * from Vehicle")
        vehicles = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        print(tabulate(vehicles,headers=headers,tablefmt="psql"))
    def GetVehicleByID(self,id):
        cursor.execute("Select * from Vehicle where VehicleID = ?",(id))
        return cursor.fetchone()
    def GetAvailableVehicle(self):
        cursor.execute("Select * from Vehicle where Availability = 1")
        vehicles = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        print(tabulate(vehicles,headers=headers,tablefmt="psql"))
    def AddVehicle(self,vehicle):
        cursor.execute("insert into Vehicle values (?,?,?,?,?,?,?)",
                       (vehicle.get_model(), vehicle.get_make(), vehicle.get_year(),
                        vehicle.get_color(), vehicle.get_registrationnumber(),
                        vehicle.get_availability(), vehicle.get_dailyrate()))
        conn.commit()
        print("Added Successfully")
    
    def UpdateVehicle(self,vehicle,vehicleid):
        cursor.execute("""
                       update vehicle
                       set Model = ?, Make = ?, Year = ?, Color = ?, RegistrationNumber = ?, Availability = ?, DailyRate = ?
                       where VehicleID = ?""",
                       (vehicle.get_model(), vehicle.get_make(), vehicle.get_year(),
                        vehicle.get_color(), vehicle.get_registrationnumber(),
                        vehicle.get_availability(), vehicle.get_dailyrate(),vehicleid))
        conn.commit()
        print("Updated Successfully")
    
    def RemoveVehicle(self,id):
        cursor.execute("delete from Vehicle where VehicleID = ?",(id))
        conn.commit()
        print("Deleted Successfully")
    
    def GetAllVehicles(self):
        cursor.execute("select * from Vehicle")
        vehicles =  cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        return vehicles, headers

# Admin Service
class AdminService:
    def GetAdmin(self,username):
        cursor.execute("select * from Admin where Username = ? ",(username))
        admin = cursor.fetchone()
        headers = [column[0] for column in cursor.description]
        print(tabulate(admin,headers=headers,tablefmt="psql"))
    def GetAdminById(self,id):
        cursor.execute("Select * from Admin where AdminID = ?",(id))
        return cursor.fetchone()
    
    def GetAdminByUsername(self,username):
        cursor.execute("select * from Admin where Username = ? ",(username))
        return cursor.fetchone()
    
    def RegisterAdmin(self,admin):
        cursor.execute("insert into Admin values(?,?,?,?,?,?,?,?)",
                       (admin.get_firstname(), admin.get_lastname(), admin.get_email(),
                        admin.get_phonenumber(), admin.get_username(), admin.get_password(),
                        admin.get_role(), admin.get_joindate()))
        conn.commit()
        print("Registered Successfully")
    
    def UpdateAdmin(self,admin,adminname):
        cursor.execute("""Update Admin
                       set FirstName = ?, LastName = ?, Email = ?, PhoneNumber = ?, Username = ?, Password = ?,
                       Role = ?, JoinDate = ?
                       where Username = ?""",
                       (admin.get_firstname(), admin.get_lastname(), admin.get_email(),
                        admin.get_phonenumber(), admin.get_username(), admin.get_password(),
                        admin.get_role(), admin.get_joindate(),adminname))
        conn.commit()
        print("Updated Successfully")
    
    def DeleteAdmin(self,adminname):
        cursor.execute("delete from Admin where Username = ?",(adminname))
        conn.commit()
        print("Deleted Successfully")

class ReservationService:
    def __init__(self,custservice,vehiserv):
        self.custservice = custservice
        self.vehiserv = vehiserv
    
    def GetReservationByID(self,reservID):
        cursor.execute("Select * from Reservation where ReservationID = ?",(reservID))
        return cursor.fetchone()
    
    def GetReservationByCustomerID(self,custid):
        cursor.execute("Select * from Reservation where CustomerID = ?",(custid))
        return cursor.fetchall()

    def GetReservationByCustomerName(self,username):
        cursor.execute("""Select ReservationID,Reservation.CustomerID,VehicleID, StartDate,EndDate,TotalCost,Status from Reservation join 
                       Customer on Reservation.CustomerID = Customer.CustomerID where Customer.Username = ? """,(username))
        return cursor.fetchall()
    def CreateReservation(self,reserv):
        vehicle = self.vehiserv.GetVehicleByID(reserv.vehicleid)
        if vehicle:
            cursor.execute("Insert into Reservation Values (?,?,?,?,?,?)",
                           (reserv.get_customerid(),reserv.get_vehicleid(),reserv.get_startdate(),reserv.get_enddate(),
                            reserv.get_totalcost(),reserv.get_status()))
            cursor.execute("update Vehicle set Availability = 0 where VehicleID = ?",reserv.vehicleid)
            conn.commit()
            print("Reservation Created Successfully")
        else:
            print("Vehicle Not Found or unavailable")
    def UpdateReservation(self,updater,reservid,reservation):
        if updater == "customer":
            cusomerid = reservation.customerid
            if self.custservice.CheckOwnership(reservid,cusomerid):
                cursor.execute("""
                               update Reservation
                               set StartDate = ?, EndDate = ?, TotalCost = ?, Status = ?
                               where ReservationID = ?""",
                               (reservation.get_startdate(),reservation.get_enddate(),
                               reservation.get_totalcost(),reservation.get_status(),reservid))
                conn.commit()
                print("Reservation Updated Successfully")
            else:
                print("Your are not authorized to update this reservation")
        elif updater == "Admin":
            cursor.execute("""
                           update Reservation
                           set CustomerID = ?, VehicleID = ?, StartDate = ?, EndDate = ?, TotalCost = ?, Status = ?
                           where ReservationID = ?""",
                           (reservation.get_customerid(),reservation.get_vehicleid(),reservation.get_startdate(),reservation.get_enddate(),
                            reservation.get_totalcost(),
                            reservation.get_status(),reservid))
            conn.commit()
            print("Reservation Updated Successfully")
    
    def CancelReservation(self,reservid):
        reservation = self.GetReservationByID(reservid)
        if reservation:
            cursor.execute("delete from Reservation where ReservationID = ?",(reservid))
            cursor.execute("update Vehicle set Availability = 1 where VehicleID = ?",(reservation[2]))
            conn.commit()
            print("Reservation Deleted Successfully")
        else:
            print("Reservation not found")
    
    def GetReservations(self):
        cursor.execute("select * from Reservation")
        reservations = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        return reservations, headers

class ReportGenerator:
    def __init__(self, reserv_service, vehicle_service):
        self.reserv_service = reserv_service
        self.vehicle_service = vehicle_service
    
    def generate_reservation_report(self):
        reservations, headers = self.reserv_service.GetReservations()
        
        if reservations:
            print(tabulate(reservations,headers=headers,tablefmt="psql"))
            total_revenue = sum(reservation[5] for reservation in reservations)
            print(f"Total Revenue: {total_revenue}")
        else:
            print("No reservations found")
    
    def generate_vehicle_report(self):
        vehicles, headers = self.vehicle_service.GetAllVehicles()
        
        if vehicles:
            print(tabulate(vehicles,headers=headers, tablefmt="psql"))
        else:
            print("No vehicles found")



def CustomerMenu():
    customerserv = CustomerService()
    authenticaeserv = AuthenticationService(customerserv)
    while(True):
        print("""
Do you want to?
1. Register
2. Login
3. Exit
 """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            newCustomer = Customer("", "", "", 0, "", "", "", "")
            newCustomer.set_firstname(input("Enter your First Name: "))
            newCustomer.set_lastname(input("Enter your Last Name: "))
            newCustomer.set_email(input("Enter your email: "))
            newCustomer.set_phonenumber(int(input("Enter your Phone number: ")))
            newCustomer.set_address(input("Enter your Address: "))
            newCustomer.set_username(input("Enter your Username: "))
            newCustomer.set_password(input("Enter your password: "))
            newCustomer.set_registrationdate(datetime.date.today())
            customerserv.RegisterCustomer(newCustomer)
        if choice == 2:
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            if authenticaeserv.authenticate_customer(username,password):
                print("Login Successful")
                print("What do you want do?")
                print("""
                      1. Update Your Account
                      2. Delete Your Account
                      3. Reservations
                      4. Go Back
                      """)
                cust_choice = int(input("Enter your Choice: "))
                if cust_choice == 1:
                    customer = customerserv.GetCustomerByUsername(username)
                    if customer:
                        ncustomer = Customer("","","",0,"","","","")
                        ncustomer.set_firstname(input("Enter your First Name: "))
                        ncustomer.set_lastname(input("Enter your Last Name: "))
                        ncustomer.set_email(input("Enter your email: "))
                        ncustomer.set_phonenumber(int(input("Enter your Phone number: ")))
                        ncustomer.set_address(input("Enter your Address: "))
                        ncustomer.set_username(input("Enter your Username: "))
                        ncustomer.set_password(input("Enter your password: "))
                        customerserv.UpdateCustomer(ncustomer, username)
                    else:
                        print("Customer not found.")
                if cust_choice == 2:
                    customerserv.GetCustomer(username)
                    print("Are you sure you want to delete? ")
                    ans = input("Type (yes) if you want to delete your account: ")
                    if ans == 'yes':
                        id = int(input("Enter your user id: "))
                        customerserv.DeleteCustomer(id)
                    else:
                        break
                if cust_choice == 3:
                    ReservationMenu(username)
                if cust_choice == 4:
                    break
            else:
                print("Invalid username or Password")
            
        if choice == 3:
            print("See you soon")
            break

def ReservationMenu(username):
    reservServ = ReservationService(CustomerService(),VehicleService())
    vehicleserv = VehicleService()
    while(True):
        print("""
 Do you want to
1. View Reservation
2. Create Reservations
3. Update Reservation
4. Cancel Reservation
5. Go back""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            reservations = reservServ.GetReservationByCustomerName(username)
            if reservations:
                print("Your Reservations: ")
                for reserve in reservations:
                    print(reserve)
            else:
                print("You dont have any reservations")
        if choice == 2:
            customerid = reservServ.custservice.GetCustomerID(username)
            print("Available Vehicles")
            vehicleserv.GetAvailableVehicle()
            vehicleid = int(input("Enter the Vehicle ID: "))
            startdate = input("Enter the Start Date (YYYY-MM-DD): ")
            enddate = input("Enter End Date (YYYY-MM-DD): ")
            vehicle = reservServ.vehiserv.GetVehicleByID(vehicleid)
            if vehicle:
                dailyrate = float(vehicle[7])
                totalcost = Reservation.CalculateTotalCost(startdate,enddate,dailyrate)
                print(f"Your Total Cost will be {totalcost}")
                status = "Pending"
                new_reservation = Reservation(0, 0, "", "", 0.00, "")
                new_reservation.set_customer_id(customerid)
                new_reservation.set_vehicle_id(vehicleid)
                new_reservation.set_start_date(startdate)
                new_reservation.set_end_date(enddate)
                new_reservation.set_total_cost(totalcost)
                new_reservation.set_status(status)
                reservServ.CreateReservation(new_reservation)
            else:
                print("Vehicle Not Found")
        if choice == 3:
            updater = "customer"
            reservations = reservServ.GetReservationByCustomerName(username)
            if reservations:
                print("Your Reservations: ")
                for reserve in reservations:
                    print(reserve)
                reserveid = int(input("Enter the Reservation ID you want to update: "))
                newStartDate = input("Enter new Start date (YYYY-MM-DD): ")
                newEndDate = input("Enter new End Date (YYYY-MM-DD): ")
                oldreserve = reservServ.GetReservationByID(reserveid)
                if oldreserve:
                    vehicle = reservServ.vehiserv.GetVehicleByID(oldreserve[2])
                    if vehicle:
                        dailyrate = float(vehicle[7])
                        newTotalCost = Reservation.CalculateTotalCost(newStartDate,newEndDate,dailyrate)
                        print(f"Your new Total Cost is {newTotalCost}")
                        new_reserve = Reservation(0, 0, "", "", 0.00, "")
                        new_reserve.set_customer_id(oldreserve[1])
                        new_reserve.set_vehicle_id(oldreserve[2])
                        new_reserve.set_start_date(newStartDate)
                        new_reserve.set_end_date(newEndDate)
                        new_reserve.set_total_cost(newTotalCost)
                        new_reserve.set_status(oldreserve[6])
                        reservServ.UpdateReservation(updater, reserveid, new_reserve)
                    else:
                        print("Vehicle Not Found")
                else:
                    print("Reservation Not Found")
            else:
                print("You dont have any reservations")
        if choice == 4:
            reservations = reservServ.GetReservationByCustomerName(username)
            if reservations:
                print("Your Reservations: ")
                for reserve in reservations:
                    print(reserve)
            reserveid = int(input("Enter the Reservation ID you want to Cancel: "))
            custChoice = input("Do you want to delete? Type (yes) if you want to: ")
            if custChoice == 'yes':
                reservServ.CancelReservation(reserveid)
            else:
                break
        else:
            break
        

def AdminMenu():
    Adminserv = AdminService()
    authenticaeserv = AuthenticationService(Adminserv)
    while(True):
        print("""
Do you want to
1. Register Admin
2. Login
3. Exit
""")
        choice = int(input("Enter your Choice: "))
        if choice == 1:
            newAdmin = Admin("", "", "", 0, "", "", "", "")
            newAdmin.set_firstname(input("Enter first name: "))
            newAdmin.set_lastname(input("Enter Last name: "))
            newAdmin.set_email(input("Enter email: "))
            newAdmin.set_phonenumber(int(input("Enter phone number: ")))
            newAdmin.set_username(input("Enter username: "))
            newAdmin.set_password(input("Enter password: "))
            newAdmin.set_role(input("Enter Role: "))
            newAdmin.set_joindate(datetime.date.today())
            Adminserv.RegisterAdmin(newAdmin)
        if choice == 2:
            username = input("Enter your Username: ")
            password = input("Enter your password: ")
            if authenticaeserv.authenticate_admin(username,password):
                print("Login Successfull")
                print("Do you want to")
                print("""
                      1. Update Your Account
                      2. Delete Your Account
                      3. Manage Vehicles
                      4. Get Report of Reservations
                      """)
                AdminChoice = int(input("Enter your choice: "))
                if AdminChoice == 1:
                    Adminserv.GetAdmin(username)
                    print("Enter Updated Details ")
                    updateAdmin = Admin("","","",0,"","","","")
                    updateAdmin.set_firstname(input("Enter first name: "))
                    updateAdmin.set_lastname(input("Enter Last name: "))
                    updateAdmin.set_email(input("Enter email: "))
                    updateAdmin.set_phonenumber(int(input("Enter phone number: ")))
                    updateAdmin.set_username(input("Enter username: "))
                    updateAdmin.set_password(input("Enter password: "))
                    updateAdmin.set_role(input("Enter Role: "))
                    date_entry = input('Enter date in YYYY-MM-DD format: ')
                    year, month, day = map(int, date_entry.split('-'))
                    updateAdmin.set_joindate(datetime.date(year, month, day))
                    Adminserv.UpdateAdmin(updateAdmin,username)
                if AdminChoice == 2:
                    Adminserv.GetAdmin(username)
                    print("Do you want to delete the account? ")
                    DelChoice = input("Type (yes) if you want to delete: ")
                    if DelChoice == 'yes':
                        Adminserv.DeleteAdmin(username)
                    else:
                        break
                if AdminChoice == 3:
                    VehicleMenu()
                if AdminChoice == 4:
                    ReportsMenu()  
            else:
                print("Invalid Username or Password")
        if choice == 3:
            print("See you again")
            break

def ReportsMenu():
    reportServ = ReportGenerator(ReservationService(CustomerService(),VehicleService()),VehicleService())
    while(True):
        print("""
Do you Want to Get:
1. Reservation Report
2. Vehicle Report
3. Go Back """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            reportServ.generate_reservation_report()
        if choice == 2:
            reportServ.generate_vehicle_report()
        if choice == 3:
            break

def VehicleMenu():
    vehicleserv = VehicleService()
    while(True):
        print("""
Do you want to?
1. Add Vehicle
2. Update Vehicle
3. Remove Vehicle
4. Go Back""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_vehicle = Vehicle("","","","","",0,0.00)
            new_vehicle.set_model(input("Enter model: "))
            new_vehicle.set_make(input("Enter make: "))
            new_vehicle.set_year(input("Enter year: "))
            new_vehicle.set_color(input("Enter color: "))
            new_vehicle.set_registrationnumber(input("Enter registration number: "))                
            new_vehicle.set_availability(int(input("Enter availability (0 or 1): ")))
            new_vehicle.set_dailyrate("{:.2f}".format(float(input("Enter daily rate: "))))
            vehicleserv.AddVehicle(new_vehicle)
        if choice == 2:
            vehicleserv.GetVehicle()
            vehicleid = int(input("Enter the Vehicle ID to update: "))
            updateVehicle = vehicleserv.GetVehicleByID(vehicleid)
            if updateVehicle:
                print("Enter Updated Details: ")
                updated_vehicle = Vehicle("","","","","",0,0.00)
                updated_vehicle.set_model(input("Enter model: "))
                updated_vehicle.set_make(input("Enter make: "))
                updated_vehicle.set_year(input("Enter year: "))
                updated_vehicle.set_color(input("Enter color: "))
                updated_vehicle.set_registrationnumber(input("Enter registration number: "))
                updated_vehicle.set_availability(int(input("Enter availability (1 - Available, 0 - Not Available): ")))
                updated_vehicle.set_dailyrate("{:.2f}".format(float(input("Enter daily rate: "))))
                vehicleserv.UpdateVehicle(updated_vehicle, vehicleid)
            else:
                print("Vehicle Not Found")
        if choice == 3:
            vehicleserv.GetVehicle()
            vehicleid = int(input("Enter the Vehicle ID to delete: "))
            delChoice = input("Are you sure? Type (yes) if you are: ")
            if delChoice == 'yes':
                vehicleserv.RemoveVehicle(vehicleid)
            else: 
                break
        if choice == 4:
            break

if __name__ == "__main__":
    while(True):
        print("Welcome to CarConnect")
        print("""
    Who are you?:
    1. Customer
    2. Admin
    3. Exit
    """)
        menu = int(input("Enter your option: "))
        if menu == 1:
            CustomerMenu()
        elif menu == 2:
            AdminMenu()
        else: 
            print("See you soon")
            break
    cursor.close()
    conn.close()

        
