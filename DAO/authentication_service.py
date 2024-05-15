from Util.DBConn import DBConnection
from Entity import Customer, Admin
class AuthenticationService(DBConnection):
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
