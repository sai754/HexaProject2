from Util.DBConn import DBConnection
from tabulate import tabulate
class AdminService(DBConnection):
    def GetAdmin(self,username):
        self.cursor.execute("select * from Admin where Username = ? ",(username))
        admin = self.cursor.fetchone()
        headers = [column[0] for column in self.cursor.description]
        print(tabulate(admin,headers=headers,tablefmt="psql"))
    def GetAdminById(self,id):
        self.cursor.execute("Select * from Admin where AdminID = ?",(id))
        return self.cursor.fetchone()
    
    def GetAdminByUsername(self,username):
        self.cursor.execute("select * from Admin where Username = ? ",(username))
        return self.cursor.fetchone()
    
    def RegisterAdmin(self,admin):
        self.cursor.execute("insert into Admin values(?,?,?,?,?,?,?,?)",
                       (admin.get_firstname(), admin.get_lastname(), admin.get_email(),
                        admin.get_phonenumber(), admin.get_username(), admin.get_password(),
                        admin.get_role(), admin.get_joindate()))
        self.conn.commit()
        print("Registered Successfully")
    
    def UpdateAdmin(self,admin,adminname):
        self.cursor.execute("""Update Admin
                       set FirstName = ?, LastName = ?, Email = ?, PhoneNumber = ?, Username = ?, Password = ?,
                       Role = ?, JoinDate = ?
                       where Username = ?""",
                       (admin.get_firstname(), admin.get_lastname(), admin.get_email(),
                        admin.get_phonenumber(), admin.get_username(), admin.get_password(),
                        admin.get_role(), admin.get_joindate(),adminname))
        self.conn.commit()
        print("Updated Successfully")
    
    def DeleteAdmin(self,adminname):
        self.cursor.execute("delete from Admin where Username = ?",(adminname))
        self.conn.commit()
        print("Deleted Successfully")