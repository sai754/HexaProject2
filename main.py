from Entity import Reservation, Customer, Admin, Vehicle, ReportGenerator
from DAO import ReservationService, AdminService, AuthenticationService, CustomerService, VehicleService
import pyodbc
import datetime 
from tabulate import tabulate


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
                new_reservation.set_customerid(customerid)
                new_reservation.set_vehicleid(vehicleid)
                new_reservation.set_startdate(startdate)
                new_reservation.set_enddate(enddate)
                new_reservation.set_totalcost(totalcost)
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
                        new_reserve.set_customerid(oldreserve[1])
                        new_reserve.set_vehicleid(oldreserve[2])
                        new_reserve.set_startdate(newStartDate)
                        new_reserve.set_enddate(newEndDate)
                        new_reserve.set_totalcost(newTotalCost)
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
def MainMenu():
    customerserv = CustomerService()
    adminserv = AdminService()
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
            customerserv.close()
            adminserv.close()
            break


if __name__ == "__main__":
    MainMenu()

        
