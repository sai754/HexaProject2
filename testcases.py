import unittest
from DAO.authentication_service import AuthenticationService
from DAO.customer_service import CustomerService
class TestCustomerAuthentication(unittest.TestCase):

    def setUp(self):
        custom_serv = CustomerService()
        self.authentication_service = AuthenticationService(custom_serv)

    def test_authentication_with_invalid_credentials(self):
        username = "invalid_username"
        password = "invalid_password"

        result = self.authentication_service.authenticate_customer(username,password)

        self.assertFalse(result, "Authentication should fail with invalid credentials")

if __name__ =="__main__":
    unittest.main()
