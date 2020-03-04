-- there are restrictions on num of characters for a valid userid, password and other fields, but it's easier to take care of that on the front end
DROP SCHEMA IF EXISTS esm_db;
CREATE SCHEMA esm_db;

-- DROP TABLE IF EXISTS student;
CREATE TABLE order
(	productID varchar(300) NOT NULL PRIMARY KEY,
	quantity varchar(300) NOT NULL,
    price varchar(300) NOT NULL,
);



LOAD DATA LOCAL INFILE 'c:/Proj/products_data.csv' INTO TABLE ordertable
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 LINES;


-- DROP TABLE IF EXISTS section;
-- CREATE TABLE section
-- (	course varchar(300) NOT NULL,
-- 	section varchar(300) NOT NULL,
--     day int(5) NOT NULL,
--     start varchar(300) NOT NULL,
--     end varchar(300) NOT NULL,
--     instructor varchar(300) NOT NULL,
--     venue varchar(300) NOT NULL,
--     size int(5) NOT NULL,
--     min_bid varchar(300) NOT NULL,
--     vacancies int(5) NOT NULL,
--     CONSTRAINT section_pk PRIMARY KEY (course, section),
--     CONSTRAINT section_fk FOREIGN KEY (course) REFERENCES course(course)
-- );

-- DROP TABLE IF EXISTS bid;
-- CREATE TABLE bid
-- (	userid varchar(300) NOT NULL,
-- 	amount varchar(300) NOT NULL,
--     code varchar(300) NOT NULL,
--     section varchar(300) NOT NULL,
--     status varchar(300) DEFAULT "Pending" NOT NULL,
--     CONSTRAINT bid_pk PRIMARY KEY (userid, code, section),
--     CONSTRAINT bid_fk1 FOREIGN KEY(userid) REFERENCES student(userid),
--     CONSTRAINT bid_fk2 FOREIGN KEY(code, section) REFERENCES section(course, section)
-- );





