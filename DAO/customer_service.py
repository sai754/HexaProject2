from Util.DBConn import DBConnection
from abc import ABC, abstractmethod
from tabulate import tabulate
from Interface import ICustomerService

class CustomerService(DBConnection, ICustomerService):

    def GetCustomer(self,username):
        self.cursor.execute("select * from Customer where Username = ?",(username))
        customer = self.cursor.fetchone()
        headers = [column[0] for column in self.cursor.description]
        print(tabulate([customer],headers=headers,tablefmt='psql'))
    def GetCustomerByID(self,id):
        self.cursor.execute("Select * from Customer where CustomerID = ?",(id,))
        return self.cursor.fetchone()

    def GetCustomerByUsername(self,username):
        self.cursor.execute("Select * from Customer where Username = ?",(username,))
        customer =  self.cursor.fetchone()
        headers = [column[0] for column in self.cursor.description]
        print(tabulate([customer],headers=headers,tablefmt='psql'))
        return customer

    def RegisterCustomer(self,newCustomer):
        self.cursor.execute("insert into Customer values (?,?,?,?,?,?,?,?)",
                    (newCustomer.get_firstname(), newCustomer.get_lastname(), newCustomer.get_email(),
                    newCustomer.get_phonenumber(), newCustomer.get_address(), newCustomer.get_username(),
                    newCustomer.get_password(), newCustomer.get_registrationdate()))
        self.conn.commit()
        print("Registered Successfully")

    def UpdateCustomer(self,customer,customername):
        self.cursor.execute("""
                    UPDATE Customer
                    SET FirstName = ?, LastName = ?, Email = ?, PhoneNumber = ?, Address = ?, Username = ?, Password = ?
                    WHERE Username = ?
                    """,
                    (customer.get_firstname(), customer.get_lastname(), customer.get_email(),
                     customer.get_phonenumber(), customer.get_address(), customer.get_username(),
                     customer.get_password(),customername))
        self.conn.commit()
        print("Updated Successfully")

    def DeleteCustomer(self,id):
        self.cursor.execute("Delete from Reservation where CustomerID = ?",(id))
        self.cursor.execute("Delete from Customer where CustomerID = ?",(id))
        self.conn.commit()
        print("Deleted Successfully")

    def CheckOwnership(self, reservation_id, customer_id):
        self.cursor.execute("SELECT CustomerID FROM Reservation WHERE ReservationID = ?", (reservation_id,))
        fetched_customer_id = self.cursor.fetchone()[0] 
        return fetched_customer_id == customer_id
    
    def GetCustomerID(self,username):
        self.cursor.execute("Select CustomerID from Customer where Username = ?",(username))
        custid = self.cursor.fetchone()[0]
        return custid
    
    def GetCustomerbyIdTest(self,username):
        self.cursor.execute("Select CustomerID from Customer where Username = ?",(username))
        custid = self.cursor.fetchone()
        return custid
    
    def CheckEmail(self, email):
        self.cursor.execute("Select count(*) from Customer where Email = ?", (email))
        count = self.cursor.fetchone()[0]
        return count > 0
