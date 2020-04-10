#### UTILTY FILE TO WIPE THE REMOTE DATABASE ####

import mysql.connector

def purge_all():
    sqldrop="DROP TABLE IF EXISTS Jobs;DROP TABLE IF EXISTS DriverInfo;CREATE TABLE DriverInfo (DID VARCHAR(10), DName VARCHAR(40),DStatus VARCHAR(10),primary key (DID));create table Jobs (JobID integer auto_increment primary key,OrderID varchar(20),Address varchar(100),DID VARCHAR(10),JStatus VARCHAR(10),telegram varchar(50),StartTime Timestamp,EndTime Timestamp,FOREIGN KEY (DID) references DriverInfo(DID));insert into DriverInfo values ('D0001','Hungry Heng', 'Offline'),('D0002', 'Sleepy AlwaysDoNightShift', 'Offline'),('D0003', 'Speedy Gonzales', 'Offline');"
    
    """ Connect to MySQL database """
    conn=None
    cursor=None
    try:
        conn = mysql.connector.connect(
        host="delivery1cc.cfom8s5f4cx6.us-east-1.rds.amazonaws.com",
        user="admin",
        passwd="ProfJiang",
        port=3306,
        database="delivery1cc")
        # conn = mysql.connector.connect(
        # host="localhost",
        # user="root",
        # passwd="",
        # port=3306,
        # database="200cc_delivery")
        if conn.is_connected():
            print('Connected to MySQL database')
 
        cursor = conn.cursor()

        sqldrop = filter(None, sqldrop.split(';'))

        for i in sqldrop:
            cursor.execute(i.strip() + ';')
        conn.commit()
        print("Purged")
    except mysql.connector.Error as error:
        print(error)
    
    if (cursor != None):
        cursor.close()
    if (conn !=None):
        conn.close() 
 
if __name__ == '__main__':
    purge_all()
