
#create inventory DB
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

CREATE SCHEMA 200cc_deliverypricing;

use 200cc_deliverypricing;

CREATE TABLE DistancePrice (Postal_Sector varchar(2),
							Region_Name varchar(100),
							Price float(6,2));

insert into DistancePrice (Postal_Sector, Region_Name, Price)
						values ('01','Raffles Place',2.50),
								('07','Anson',2.70),
                                ('14','Queenstown',3.20),
                                ('10','Harbourfront',3.40),
                                ('11','Pasir Panjang',4.00),
                                ('17','High Street',3.70),
                                ('20','Little India',3.30),
                                ('22','Orchard',2.80),
                                ('25','Bukit Timah',4.40),
                                ('30','Thomson',3.50),
                                ('31','Balestier',3.60),
                                ('46','Bedok',4.20),
                                ('51','Tampines',4.70);
                                
                                
                            
                        

                        


