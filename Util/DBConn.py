import pyodbc
from Util.DBPropertyUtil import PropertyUtil

DB = PropertyUtil.getProperty()


class DBConnection:
    def __init__(self):
        self.conn = pyodbc.connect(DB)
        self.cursor = self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()