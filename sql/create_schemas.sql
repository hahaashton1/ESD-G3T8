#NOTE#
#
# you dont need to create all the schema on your local machine. just create whatever schema is necessary for the microservice you are working on
# any problems lemme know :) @tsueanne (Telegram)
#

CREATE SCHEMA 200cc_inventory;

use 200cc_inventory;

CREATE TABLE Product (PID VARCHAR(10) primary key, 
					PName VARCHAR(50), 
                    Quantity SMALLINT);

#############################################################

CREATE SCHEMA 200cc_order;

use 200cc_order;

CREATE TABLE ProductPrice (PID VARCHAR(10), 
							Price FLOAT(6,2),
                            primary key (PID));
                            
CREATE TABLE DriverInfo (DID VARCHAR(10), 
						DName VARCHAR(40),
						primary key (DID));
                        
CREATE TABLE OrderInfo (OrderID VARCHAR(20),
						CID varchar(10),
                        PID varchar(10),
                        Address varchar(100),
                        DriverID varchar(10),
                        primary key (OrderID),
						FOREIGN KEY (DriverID) REFERENCES DriverInfo(DID),
                        FOREIGN KEY (PID) references ProductPrice(PID)
                        );
                        
#############################################################

CREATE SCHEMA 200cc_customer;

use 200cc_customer;

CREATE TABLE Customer (CID VARCHAR(10), 
						CName VARCHAR(40),
                        CCNo VARCHAR(20),
                        Address VARCHAR(100),
						Phone VARCHAR(20),
						primary key (CID));

#############################################################

CREATE SCHEMA 200cc_deliverypricing;

use 200cc_deliverypricing;

CREATE TABLE DistancePrice (distance float(6,2),
							price float(6,2));
                            
                        

                        


