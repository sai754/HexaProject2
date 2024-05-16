from datetime import datetime
class Reservation:
    def __init__(self,customerid,vehicleid,startdate,enddate,totalcost,status):
        self.__customerid = customerid
        self.__vehicleid = vehicleid
        self.__startdate = startdate
        self.__enddate = enddate
        self.__totalcost = totalcost
        self.__status = status


    def get_customerid(self):
        return self.__customerid

    def get_vehicleid(self):
        return self.__vehicleid

    def get_startdate(self):
        return self.__startdate

    def get_enddate(self):
        return self.__enddate

    def get_totalcost(self):
        return self.__totalcost

    def get_status(self):
        return self.__status
    
    def set_customerid(self, customerid):
        self.__customerid = customerid

    def set_vehicleid(self, vehicleid):
        self.__vehicleid = vehicleid

    def set_startdate(self, startdate):
        self.__startdate = startdate

    def set_enddate(self, enddate):
        self.__enddate = enddate

    def set_totalcost(self, totalcost):
        self.__totalcost = totalcost

    def set_status(self, status):
        self.__status = status

    
    def CalculateTotalCost(startdate,enddate,dailyrate):
        startdate = datetime.strptime(startdate,"%Y-%m-%d")
        enddate = datetime.strptime(enddate,"%Y-%m-%d")
        numdays = (enddate - startdate).days
        totalcost = numdays * dailyrate
        return totalcost