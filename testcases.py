import unittest
from DAO.authentication_service import AuthenticationService
from DAO.customer_service import CustomerService
from Entity import Customer
class TestCustomerAuthentication(unittest.TestCase):

    def setUp(self):
        Custom_serv = CustomerService()
        self.custom_serv = CustomerService()
        self.authentication_service = AuthenticationService(Custom_serv)

    def test_authentication_with_invalid_credentials(self):
        username = "invalid_username"
        password = "invalid_password"

        result = self.authentication_service.authenticate_customer(username,password)

        self.assertFalse(result, "Authentication should fail with invalid credentials")

    def test_update_customer_inforamtion(self):
        new_customer = Customer(firstname="ABC", lastname="EFG", email="qqq@example.com",
                                   phonenumber=1234567890, address="India", 
                                   username="abc", password="abcde123", registrationdate="2024-05-16")
        
        self.custom_serv.RegisterCustomer(new_customer)

        updated_customer = Customer(firstname="ABC", lastname="QAV", email="qqq@example.com",
                                     phonenumber=9876543210, address="India", 
                                     username="abc", password="newpassword", registrationdate="2024-05-16")
        
        self.custom_serv.UpdateCustomer(updated_customer, "abc")
        retrieved_customer = self.custom_serv.GetCustomerByUsername("abc")

        self.assertEqual(retrieved_customer[2], "QAV")
        self.assertEqual(retrieved_customer[3], "qqq@example.com")
        self.assertEqual(retrieved_customer[4], 9876543210)
        self.assertEqual(retrieved_customer[5], "India")
        self.assertEqual(retrieved_customer[6], "abc")
        self.assertEqual(retrieved_customer[7], "newpassword")

    def tearDown(self):
        customer_id = self.custom_serv.GetCustomerID("abc")
        self.custom_serv.DeleteCustomer(customer_id)
        print("Deleted Successfully")
    
    

if __name__ =="__main__":
    unittest.main()
