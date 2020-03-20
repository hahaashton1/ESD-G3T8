
#create inventory DB
DROP SCHEMA IF EXISTS 200cc_inventory;
CREATE SCHEMA 200cc_inventory;

use 200cc_inventory;

CREATE TABLE Product (PID VARCHAR(10) primary key, 
					PName VARCHAR(50), 
                    Quantity SMALLINT);

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
                    JStatus VARCHAR(10),
                    telegram varchar(50),
                    StartTime Timestamp,
                    EndTime Timestamp,
                    FOREIGN KEY (DID) references DriverInfo(DID)
                    );
                                       

insert into DriverInfo values ('D0001','Hungry Heng', 'Offline'),
							('D0002', 'Sleepy AlwaysDoNightShift', 'Offline'),
                            ('D0003', 'Speedy Gonzales', 'Offline');


#############################################################
DROP SCHEMA IF EXISTS 200cc_deliverypricing;
CREATE SCHEMA 200cc_deliverypricing;

use 200cc_deliverypricing;

CREATE TABLE DistancePrice (Postal_Sector varchar(2),
							Region_Name varchar(100),
							Price float(6,2));

LOAD DATA LOCAL INFILE 'C:/wamp64/www/ESD-G3T8/sql/delivery_pricing.csv' INTO TABLE DistancePrice
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 LINES;                            




                            
                        

                        


