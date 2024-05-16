import unittest
from DAO import CustomerService, VehicleService, AuthenticationService
from Entity import Customer, Vehicle
# class TestCustomerAuthentication(unittest.TestCase):

#     def setUp(self):
#         Custom_serv = CustomerService()
#         self.custom_serv = CustomerService()
#         self.authentication_service = AuthenticationService(Custom_serv)

#     def test_authentication_with_invalid_credentials(self):
#         username = "invalid_username"
#         password = "invalid_password"

#         result = self.authentication_service.authenticate_customer(username,password)

#         self.assertFalse(result, "Authentication should fail with invalid credentials")

#     def test_update_customer_inforamtion(self):
#         new_customer = Customer(firstname="ABC", lastname="EFG", email="qqq@example.com",
#                                    phonenumber=1234567890, address="India", 
#                                    username="abc", password="abcde123", registrationdate="2024-05-16")
        
#         self.custom_serv.RegisterCustomer(new_customer)

#         updated_customer = Customer(firstname="ABC", lastname="QAV", email="qqq@example.com",
#                                      phonenumber=9876543210, address="India", 
#                                      username="abc", password="newpassword", registrationdate="2024-05-16")
        
#         self.custom_serv.UpdateCustomer(updated_customer, "abc")
#         retrieved_customer = self.custom_serv.GetCustomerByUsername("abc")

#         self.assertEqual(retrieved_customer[2], "QAV")
#         self.assertEqual(retrieved_customer[3], "qqq@example.com")
#         self.assertEqual(retrieved_customer[4], 9876543210)
#         self.assertEqual(retrieved_customer[5], "India")
#         self.assertEqual(retrieved_customer[6], "abc")
#         self.assertEqual(retrieved_customer[7], "newpassword")

#     def tearDown(self):
#         customer_id = self.custom_serv.GetCustomerID("abc")
#         self.custom_serv.DeleteCustomer(customer_id)
#         print("Deleted Successfully")

class TestVehcile(unittest.TestCase):

    def setUp(self):
        self.vehicle_service = VehicleService()

    def test_add_new_vehcile(self):
        newVehicle = Vehicle(model="ABC", make="XYZ",year="2018",color="blue",registrationnumber="ASDF123",availability=1,dailyrate=50.00)

        self.vehicle_service.AddVehicle(newVehicle)

        retrivedVehicle = self.vehicle_service.GetVehicleByRegistrationNumber("ASDF123")
        self.assertEqual(retrivedVehicle[1],"ABC")
        self.assertEqual(retrivedVehicle[2],"XYZ")

    def test_update_vehicle(self):
        newVehicle = Vehicle(model="ABC", make="XYZ",year="2018",color="blue",registrationnumber="ASDF123",availability=1,dailyrate=50.00)
        self.vehicle_service.AddVehicle(newVehicle)
        retrivedVehicle = self.vehicle_service.GetVehicleByRegistrationNumber("ASDF123")
        updateVehicle = Vehicle(model="DEF", make="AAA",year="2018",color="blue",registrationnumber="ASDF123",availability=1,dailyrate=50.00)
        self.vehicle_service.UpdateVehicle(updateVehicle,retrivedVehicle[0])
        retrivedUpdatedVehicle = self.vehicle_service.GetVehicleByRegistrationNumber("ASDF123")
        self.assertEqual(retrivedUpdatedVehicle[1],"DEF")
        self.assertEqual(retrivedUpdatedVehicle[2],"AAA")
        
    def tearDown(self):
        retrivedVehicle = self.vehicle_service.GetVehicleByRegistrationNumber("ASDF123")
        self.vehicle_service.RemoveVehicle(retrivedVehicle[0])

    
    

if __name__ =="__main__":
    unittest.main()
