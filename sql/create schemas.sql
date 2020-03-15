
#create inventory DB
DROP SCHEMA IF EXISTS 200cc_inventory;
CREATE SCHEMA 200cc_inventory;

use 200cc_inventory;

CREATE TABLE Product (PID VARCHAR(10) primary key, 
					PName VARCHAR(50), 
                    Quantity SMALLINT,
                    Price float(6,2));

insert into Product (PID, PName, Quantity, Price)
						values ('01', 'Chocolate', 15, 2.00),
                        ('02', 'Stawberry', 36, 2.50),
                        ('03', 'Vanilla', 42, 2.30),
                        ('04', 'Coconut', 12, 2.30),
                        ('05', 'Raspberry', 34, 2.30),
                        ('06', 'Watermelon', 23, 2.90),
                        ('07', 'Honeydew', 43, 2.90);

#############################################################
DROP SCHEMA IF EXISTS 200cc_order;
CREATE SCHEMA 200cc_order;

use 200cc_order;

CREATE TABLE ProductPrice (PID VARCHAR(10), 
							Price FLOAT(6,2),
                            primary key (PID));
                            
CREATE TABLE Customer (CID VARCHAR(10), 
						CName VARCHAR(40),Address varchar(100),
                        CCNo VARCHAR(20),
                        CVV VARCHAR(3),
						Phone VARCHAR(20),
						primary key (CID));
                        
CREATE TABLE OrderInfo (OrderID VARCHAR(20),
						CID varchar(10),
                        PID varchar(10),
                        Quantity SMALLINT,
                        Address varchar(100),
                        primary key (OrderID),
                        FOREIGN KEY (PID) references ProductPrice(PID),
						FOREIGN KEY (CID) references Customer(CID)
                        );
                        
#############################################################
DROP SCHEMA IF EXISTS 200cc_delivery;
CREATE SCHEMA 200cc_delivery;

use 200cc_delivery;

CREATE TABLE DriverInfo (DID VARCHAR(10), 
						DName VARCHAR(40),
                        DStatus VARCHAR(10),
						primary key (DID));
                        
create table Jobs (JobID integer auto_increment primary key,
					OrderID varchar(20),
					Address varchar(100),
                    DID VARCHAR(10),
                    Completed boolean,
                    FOREIGN KEY (DID) references DriverInfo(DID)
                    );
                                       

insert into DriverInfo values ('D0001','Hungry Heng', 'Offline'),
							('D0002', 'Sleepy AlwaysDoNightShift', 'Offline'),
                            ('D0003', 'Speedy Gonzales', 'Offline');


#############################################################
DROP SCHEMA IF EXISTS 200cc_deliverypricing;
CREATE SCHEMA 200cc_deliverypricing;

use 200cc_deliverypricing;

CREATE TABLE DistancePrice (
							Region_Name varchar(100),
							Price float(6,2)
                            );

insert into DistancePrice (Region_Name, Price)
						values ('Central',2.50),
								('East',2.70),
                                ('North',3.20),
                                ('North-East',3.40),
                                ('West',4.00);
                                
                                
                            
                        

                        


