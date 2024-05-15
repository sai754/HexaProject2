import pyodbc
from Util.DBPropertyUtil import PropertyUtil
from Exceptions.exceptions import DatabaseConnectionException

DB = PropertyUtil.getProperty()


class DBConnection:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(DB)
            self.cursor = self.conn.cursor()
        except DatabaseConnectionException as e:
            print(e)
    def close(self):
        self.cursor.close()
        self.conn.close()