from Entity import Reservation, Customer, Admin, Vehicle, ReportGenerator
from DAO import ReservationService, AdminService, AuthenticationService, CustomerService, VehicleService, Validation
from datetime import datetime, date
from tabulate import tabulate
from Exceptions.exceptions import VehicleNotFoundException
from Exceptions.exceptions import InvalidInputException


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
        try: 
            choice = int(input("Enter your choice: "))
        except ValueError:
            raise InvalidInputException("Choice must be integer")
        
        if choice == 1:
            newCustomer = Customer("", "", "", 0, "", "", "", "")
            try:
                newCustomer.set_firstname(input("Enter your First Name: "))
                newCustomer.set_lastname(input("Enter your Last Name: "))
                email = input("Enter your email: ")
                if not Validation.is_valid_email(email):
                    raise InvalidInputException("Invalid Email Format")
                if customerserv.CheckEmail(email):
                    print("Email Already Exists")
                    break
                newCustomer.set_email(email)
                newCustomer.set_phonenumber(int(input("Enter your Phone number: ")))
                newCustomer.set_address(input("Enter your Address: "))
                newCustomer.set_username(input("Enter your Username: "))
                password = input("Enter your password (atleast 8 characters, must have both number and character): ")
                if not Validation.is_valid_password(password):
                    raise InvalidInputException("Password must be 8 characters long and must have both character and number")
                newCustomer.set_password(password)
                newCustomer.set_registrationdate(date.today())
                customerserv.RegisterCustomer(newCustomer)
            except InvalidInputException as e:
                print(e)
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
                        try: 
                            ncustomer = Customer("","","",0,"","","","")
                            ncustomer.set_firstname(input("Enter your First Name: "))
                            ncustomer.set_lastname(input("Enter your Last Name: "))
                            email = input("Enter your email: ")
                            if not Validation.is_valid_email(email):
                                raise InvalidInputException("Invalid email format.")
                            if customerserv.CheckEmail(email):
                                print("Email Already Exists")
                                break
                            ncustomer.set_email(email)
                            ncustomer.set_phonenumber(int(input("Enter your Phone number: ")))
                            ncustomer.set_address(input("Enter your Address: "))
                            ncustomer.set_username(input("Enter your Username: "))
                            ncustomer.set_password(input("Enter password (Should be 8 Charachters long and have both character and numbers): "))
                            customerserv.UpdateCustomer(ncustomer, username)
                        except InvalidInputException as e:
                            print(e)
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
                    while(True):
                        ReservationMenu(username)
                        goBack = int(input("If you want to Go Back press 1 else press 2: "))
                        if goBack == 1:
                            break
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
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            raise InvalidInputException("Choice must be an integer.")
        if choice == 1:
            reservations = reservServ.GetReservationByCustomerName(username)
            if reservations:
                print("Your Reservations are Above ")
            else:
                print("You dont have any reservations")
        if choice == 2:
            customerid = reservServ.custservice.GetCustomerID(username)
            print("Available Vehicles")
            vehicleserv.GetAvailableVehicle()
            vehicleid = int(input("Enter the Vehicle ID: "))
            startdate = input("Enter the Start Date (YYYY-MM-DD): ")
            enddate = input("Enter End Date (YYYY-MM-DD): ")
            if Validation.is_valid_date(startdate) and Validation.is_valid_date(enddate) == False:
                print("Invalid Date Format")
                break
            else:
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
                if Validation.is_valid_date(startdate) and Validation.is_valid_date(enddate) == False:
                    print("Invalid Date Format")
                    break
                newStatus = input("Enter your Status (Confirmed or Pending)")
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
                        new_reserve.set_status(newStatus)
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
    reservServ = ReservationService(CustomerService(),VehicleService())

    while(True):
        print("""
Do you want to
1. Register Admin
2. Login
3. Exit
""")  
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            raise InvalidInputException("Choice must be an integer.")
        if choice == 1:
            newAdmin = Admin("", "", "", 0, "", "", "", "")
            newAdmin.set_firstname(input("Enter first name: "))
            newAdmin.set_lastname(input("Enter Last name: "))
            email = input("Enter email: ")
            if not Validation.is_valid_email(email):
                raise InvalidInputException("Invalid email format.")
            if Adminserv.CheckEmail(email):
                print("Email Already Exists")
                break
            newAdmin.set_email(email)
            newAdmin.set_phonenumber(int(input("Enter phone number: ")))
            newAdmin.set_username(input("Enter username: "))
            password = input("Enter password (Should be 8 Charachters long and have both character and numbers): ")
            if not Validation.is_valid_password(password):
                raise InvalidInputException("Password must be at least 8 characters long and contain both letters and numbers.")
            newAdmin.set_password(password)
            newAdmin.set_role(input("Enter Role: "))
            newAdmin.set_joindate(date.today())
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
                      5. Go Back
                      """)
                AdminChoice = int(input("Enter your choice: "))
                if AdminChoice == 1:
                    Adminserv.GetAdmin(username)
                    print("Enter Updated Details ")
                    updateAdmin = Admin("","","",0,"","","","")
                    updateAdmin.set_firstname(input("Enter first name: "))
                    updateAdmin.set_lastname(input("Enter Last name: "))
                    email = input("Enter email: ")
                    if not Validation.is_valid_email(email):
                        raise InvalidInputException("Invalid email format.")
                    if Adminserv.CheckEmail(email):
                        print("Email Already Exists")
                        break
                    updateAdmin.set_email(email)
                    updateAdmin.set_phonenumber(int(input("Enter phone number: ")))
                    updateAdmin.set_username(input("Enter username: "))
                    updateAdmin.set_password(input("Enter password (Should be 8 Charachters long and have both character and numbers):"))
                    updateAdmin.set_role(input("Enter Role: "))
                    updateAdmin.set_joindate("")
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
                if AdminChoice == 5:
                    break
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
            try:
                new_vehicle.set_model(input("Enter model: "))
                new_vehicle.set_make(input("Enter make: "))
                new_vehicle.set_year(input("Enter year: "))
                new_vehicle.set_color(input("Enter color: "))
                new_vehicle.set_registrationnumber(input("Enter registration number: "))                
                new_vehicle.set_availability(int(input("Enter availability (0 or 1): ")))
                new_vehicle.set_dailyrate("{:.2f}".format(float(input("Enter daily rate: "))))
                vehicleserv.AddVehicle(new_vehicle)
            except Exception as e:
                raise InvalidInputException(str(e))
        if choice == 2:
            vehicleserv.GetVehicle()
            try:
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
                    available = int(input("Enter availability (1 - Available, 0 - Not Available): "))
                    if available not in (1,0):
                        print("Enter only 1 or 0")
                        break
                    updated_vehicle.set_availability(available)
                    updated_vehicle.set_dailyrate("{:.2f}".format(float(input("Enter daily rate: "))))
                    vehicleserv.UpdateVehicle(updated_vehicle, vehicleid)
                else:
                    raise VehicleNotFoundException
            except VehicleNotFoundException as e:
                print(e)
        if choice == 3:
            vehicleserv.GetVehicle()
            try:
                vehicleid = int(input("Enter the Vehicle ID to delete: "))
                delChoice = input("Are you sure? Type (yes) if you are: ")
                if delChoice == 'yes':
                    vehicleserv.RemoveVehicle(vehicleid)
                else: 
                    break
            except ValueError:
                raise InvalidInputException("Vehicle ID must be Integer")
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

        
