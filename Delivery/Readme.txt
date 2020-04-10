DELIVERY MS + DRIVER UI

delivery_ms:
- delivery.py (code)
- files related to dockerbuild. use the dockerfile to build an image.

driver_ui:
- driver.py (code)
- files related to dockerbuild. use the dockerfile to build an image.

obsolete files:
-like it says. old version of delivery_ms using flask (not amqp). 
included here for reference only.

utilities: 
- ordertrigger.py: generates fake orders and pushes them to delivery. used for testing delivery ms+driver ui.
- wipe_all: resets the remote RDS database to its initial state (clears all jobs, does not clear 3x test drivers).


HOW TO RUN THE DELIVERY MICROSERVICE:

*** If you would like to try the service running on MS Server 2019, please let me (@tsueanne) know so I can start the service for you.
*** The instructions below are for starting all services on the local machine. The version of Delivery MS on server is identical to the one in the folder.

1. Start the container of delivery.py. You will see a welcome message.

2. Once delivery is started, it will need jobs to run. 
You can either push a job from the Cafe UI -> Order MS, or use the ordertrigger.py (Testing utility) to generate jobs for it.
To use the ordertrigger.py utility, run the ordertrigger.py file. It will use a timer to generate jobs and push them to the Delivery MS.

3. There are jobs now being pushed to Delivery but there are no Drivers to take them. Start the container of Driver UI

4. Driver UI will prompt you to login. Please log in with the following test DriverIDs: D0001, D0002 or D0003. 
Please dont use any other value to log in, it will be rejected (You can try but Delivery MS will just terminate you)

5. You may open more instances of Driver MS and login with different DriverIDs if you wish.

6. Once connected, Delivery will start pushing any available jobs to the connected Drivers. You don't need to do anything as the fulfilment of the jobs 
are automated by a timer to simulate the completion of the job.

7. After job is completed, Delivery will display a message. Please note if you are using ordertrigger.py, a telegram message will be sent to my (Sue-Anne's)
Telegram account! Thus you won't get to see it. Please see below on how to set the Telegram ID to your own.

8. To terminate the services, stop the containers.
Please terminate Driver MS before terminating Delivery MS. Technically doing the other way is ok, but the Driver MS will send a message to Delivery MS 
notifying that it has left. If you terminate Delivery MS before that, the message is persistent and will be received the next time you open Delivery MS. 
Not a huge problem as it does not interfere with the operation of the next run, but it looks unsightly.
Try not to terminate Driver when it is in the middle of fulfilling a job as the job will be forever stuck as being in progress (Delivery MS will not 
reassign the job to another driver if it has already been accepted before).


USING YOUR OWN DETAILS (E.G. TELEGRAM ID)

Whether you use ordertrigger.py or Cafe UI to create the job, you may want to use your own Telegram ID to see if you can receive messages.
Please note that the telegram ID is not your telegram handle @name! You can locate your telegram ID by issuing command /start and /getid to @myidbot
Due to Telegram's restrictions, we can only send messages to you if you allow us to. So please go to @G1T8cupcakebot and issue us command /start before we 
can message you.
There isn't any way to work around this as Telegram meant it to protect you from spam :) 


HELP? NEED A DEMO?

If you have difficulty getting this to work or would like a demo, please contact @tsueanne ^^
