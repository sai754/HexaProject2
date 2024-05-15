from Util.DBConn import DBConnection
from tabulate import tabulate
from abc import abstractmethod,ABC
from Exceptions.exceptions import AdminNotFoundException

class IAdminService(ABC):
    @abstractmethod
    def GetAdminById(adminId):
        pass
    @abstractmethod
    def GetAdminByUsername(username):
        pass
    @abstractmethod
    def RegisterAdmin(adminData):
        pass
    @abstractmethod
    def UpdateAdmin(adminData,adminName):
        pass
    @abstractmethod
    def DeleteAdmin(adminName):
        pass
class AdminService(DBConnection):
    def GetAdmin(self,username):
        self.cursor.execute("select * from Admin where Username = ? ",(username))
        admin = self.cursor.fetchone()
        if admin:
            headers = [column[0] for column in self.cursor.description]
            print(tabulate([admin],headers=headers,tablefmt="psql"))
        else:
            raise AdminNotFoundException(f"Admin with username {username} not found")
    def GetAdminById(self,id):
        try:
            self.cursor.execute("Select * from Admin where AdminID = ?",(id))
            admin = self.cursor.fetchone()
            if len(admin) == 0:
                raise AdminNotFoundException
            return admin
        except AdminNotFoundException as e:
            print(e)
    
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