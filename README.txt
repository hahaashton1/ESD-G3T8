README

Please start wampserver to run the service, and ensure you have a working internet connection.

Please run these from localhost:
\Bakery_UI\index.php - Start page of Bakery UI
\Order\delivery_pricing.py - Delivery Pricing Microservice

Please build the dockerfile located in \Order, and use this to run the Order microservice.

You can run Delivery Microservice on localhost or on server. 
If you wish to run on server, pls contact @tsueanne to start the service for you (needs access key and secret key to log in, which is not static)
If you wish to run on localhost, build the dockerfile at \Delivery\delivery_ms and run the container.

Build the container at \Delivery\driver_ui\ and use it to run the Driver microservice.
You can run up to 3 instances of driver.py with the following test details:
DriverID: D0001
DriverID: D0002
DriverID: D0003
When Driver microservice is started, it will prompt you to enter the above DriverIDs to log in.

(Note: Delivery MS and Driver UI have their own detailed Readme, located in the /Delivery folder)




PASSWORDS FOR DATABASES:

Delivery Microservice Database
Endpoint: delivery1cc.cfom8s5f4cx6.us-east-1.rds.amazonaws.com
Username: admin
Password:ProfJiang
Port: 3306
Schema: delivery1cc


DeliveryPricing, Twitter and Order Microservice Database
Endpoint: orders-db.cvjwtqqbkq8r.ap-southeast-1.rds.amazonaws.com
Username: admin
Password:password
Port: 3306
Schema: cc_pricing, cc_twitter, 200cc