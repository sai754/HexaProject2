use CarConnect;

CREATE TABLE [Customer] (
  [CustomerID] Int identity(1,1),
  [FirstName] Varchar(50),
  [LastName] Varchar(50),
  [Email] Varchar(70),
  [PhoneNumber] BigInt,
  [Address] Varchar(255),
  [Username] Varchar(255),
  [Password] Varchar(255),
  [RegistrationDate] Date,
  PRIMARY KEY ([CustomerID])
);

CREATE TABLE [Vehicle] (
  [VehicleID] Int identity(1,1),
  [Model] Varchar(50),
  [Make] Varchar(50),
  [Year] Date,
  [Color] Varchar(50),
  [RegistrationNumber] Varchar(50),
  [Availability] bit,
  [DailyRate] Decimal(5,2),
  PRIMARY KEY ([VehicleID])
);

CREATE TABLE [Reservation] (
  [ReservationID] Int identity(1,1),
  [CustomerID] Int,
  [VehicleID] Int,
  [StartDate] Date,
  [EndDate] Date,
  [TotalCost] Decimal(10,2),
  [Status] Varchar(20),
  PRIMARY KEY ([ReservationID]),
  Foreign Key ([CustomerID]) references Customer([CustomerID]),
  Foreign Key ([VehicleID]) references Vehicle([VehicleID])
);

CREATE TABLE [Admin] (
  [AdminID] Int identity(1,1),
  [FirstName] Varchar(50),
  [LastName] Varchar(50),
  [Email] Varchar(50),
  [PhoneNumber] BigInt,
  [Username] Varchar(50),
  [Password] Varchar(50),
  [Role] Varchar(50),
  [JoinDate] Date,
  PRIMARY KEY ([AdminID])
);




insert into Customer values 
('Sai','Chandra','abc@example.com',1324567890,'Ambattur, Chennai','SaiSC','sai27021','2024-04-09'),
('Rex','Milan','cde@example.com',1344456890,'Tamabaram, Chennai','RexM','123rexmilan','2024-04-08');

insert into Vehicle values
('Civic','Honda','2018','White','ABCD123',1,50.00),
('Virtus','Volkswagen','2022','Black','CDEF582',0,70.00);

insert into Reservation values
(1,1,'2024-04-18','2024-04-20',150.00,'Completed'),
(2,2,'2024-05-12','2024-05-15',280.00,'Confirmed');

insert into [Admin] values
('Alen','Babu','xyz@example.com',7254456139,'alenJB','babu9876','Admin','2024-02-05'),
('Akash','MR','jsk@example.com',6356123972,'akashMR','akash345','DB Admin','2024-03-20');

select * from Customer;
select * from Vehicle;
select * from Admin;
select * from Reservation;

delete from Customer where FirstName = 'ABC'

Select ReservationID,Reservation.CustomerID,VehicleID, StartDate,EndDate,TotalCost,Status from Reservation join Customer on Reservation.CustomerID = Customer.CustomerID
where Customer.Username = 'SaiSC';

delete from Admin where AdminID = 4

delete from Vehicle where VehicleID = 8

select c.CustomerID, c.FirstName, v.Model, v.Make, c.Email, c.Address, r.ReservationID, r.VehicleID, r.TotalCost, r.Status, 
r.EndDate from Reservation r join Customer c on 
r.CustomerID = c.CustomerID join Vehicle v on r.VehicleID = v.VehicleID; 