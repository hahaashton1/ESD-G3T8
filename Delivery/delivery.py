#### DELIVERY MS ####

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import pika
import json
import time
import multiprocessing
import atexit
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/200cc_delivery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

hostname = "localhost"
port = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))

channel = connection.channel()

exchangename="delivery_exchange"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

class Driver_Info(db.Model):
    __tablename__= 'driverinfo'

    did=db.Column(db.String(10),primary_key=True)
    dname=db.Column(db.String(40),nullable=False)
    dstatus=db.Column(db.String(10), nullable=False)

class Jobs(db.Model):
    __tablename__= 'jobs'
    JobID=db.Column(db.Integer, primary_key=True)
    OrderID=db.Column(db.String(20),nullable=False)
    Address=db.Column(db.String(100),nullable=False)
    did=db.Column(db.String(10),nullable=True)
    jstatus=db.Column(db.String, nullable=False) 
    starttime=db.Column(db.DateTime, nullable=True)
    endtime=db.Column(db.DateTime, nullable=False)

incompletejobs=None

def initiate_listening():
    channelqueue=channel.queue_declare(queue="delivery", durable=True)
    queue_name=channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='delivery')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) 
    channel.start_consuming()

def validateDriver(driver_id):
    print("Driver " +driver_id+ " is attempting to connect.")
    this_driver=Driver_Info.query.filter(Driver_Info.did==str(driver_id)).first()
    if this_driver:
        #update the database
        Driver_Info.query.filter_by(did=driver_id).first().dstatus="Available"
        db.session.commit()

        print("Driver " +driver_id+ " successfully connected.")
        #inform driver ms
        channel.queue_declare(queue="driver", durable=True)
        channel.queue_bind(exchange=exchangename, queue="driver", routing_key=driver_id+".driver")
        channel.basic_publish(exchange=exchangename, routing_key=driver_id+".driver", body=json.dumps(["validate",True]),
            properties=pika.BasicProperties(delivery_mode=2))
    else:
        #send it back not ok
        print("Driver " +driver_id+ " authentication failed.")
        print("Driver " +driver_id+ " left.")
        channel.queue_declare(queue="driver", durable=True)
        channel.queue_bind(exchange=exchangename, queue="driver", routing_key=driver_id+".driver")        
        channel.basic_publish(exchange=exchangename, routing_key=driver_id+".driver", body=json.dumps(["validate",False]),
            properties=pika.BasicProperties(delivery_mode=2))

def send_order_to_driver(driver_id, orderid, address):
    channel.queue_declare(queue="driver", durable=True)
    channel.queue_bind(exchange=exchangename, queue="driver", routing_key=driver_id+".driver")        
    channel.basic_publish(exchange=exchangename, routing_key=driver_id+".driver", body=json.dumps(["order",[orderid, address]]),
        properties=pika.BasicProperties(delivery_mode=2))

def assign_driver_to_order(newjob):
    available_drivers=Driver_Info.query.filter_by(dstatus="Available").all()
    if not available_drivers:
        print("No drivers available.")
        #set status to uncompleted in db
        Jobs.query.filter_by(OrderID=newjob.OrderID).first().jstatus="Incomplete"
        db.session.commit()
    else:
        if len(available_drivers)==0:
            randomdriver=available_drivers[0]
        else:
            randomdriver=available_drivers[random.randint(0,len(available_drivers)-1)]
        #update database
        Driver_Info.query.filter_by(did=randomdriver.did).first().dstatus="Engaged"
        newjob.did=randomdriver.did           
        #send order to chosen driver
        send_order_to_driver(randomdriver.did, newjob.OrderID, newjob.Address)
        Jobs.query.filter_by(OrderID=newjob.OrderID).first().jstatus="Driving"
        print("Order", newjob.OrderID, "assigned to", newjob.did)
        db.session.commit()
        return True
    return False

def callback(channel, method, properties, body): 
    # REFER TO HERE FOR HOW ALL THE DIFFERENT MESSAGES ARE HANDLED #
    # i will move them to their own functions if it gets too messy
    raw_message=json.loads(body)
    key=raw_message[0]
    message=raw_message[1]
    if (key=='validate'):
        validateDriver(message)
    elif (key=="exit"):
        #update the database
        Driver_Info.query.filter_by(did=message).first().dstatus="Offline"
        db.session.commit()
        print("Driver " +message+ " left.")
        ### what to do if driver that is engaged leaves without completing job?
    elif (key=="order"):
        thisorderid=message[0]
        thisaddress=message[1]
        # insert order to database
        newjob=Jobs(OrderID=thisorderid, Address=thisaddress, did=None, jstatus="Pending", starttime=datetime.datetime.now())
        db.session.add(newjob)
        db.session.commit()
        print("Order recorded:", message)
        #assign to driver
        if assign_driver_to_order(newjob)==False:
            global incompletejobs
            incompletejobs.value+=1
    elif (key=="completed"):
        completed_userid=message[0]
        completed_orderid=message[1]
        print("Order", completed_orderid, "has been delivered by", completed_userid)
        #release driver
        Driver_Info.query.filter_by(did=completed_userid).first().dstatus="Available"
        #complete order
        thisJob=Jobs.query.filter_by(OrderID=completed_orderid).first()
        thisJob.jstatus="Completed"
        thisJob.endtime=datetime.datetime.now()
        db.session.commit()

def worker_check_unassignedjobs(incompletejobs):
    while (True):
        ijobs=incompletejobs.value
        print("Fantasma was here", ijobs)
        #get order from database
        if ijobs > 0:
            undonejob=Jobs.query.filter_by(jstatus="Incomplete").first()
            thisorderid=undonejob.OrderID
            thisaddress=undonejob.Address
            print("Trying order", thisorderid, "again:", thisaddress)
            if (assign_driver_to_order(undonejob)):
                incompletejobs.value-=1
        time.sleep(8)

#atexit.register()


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nWELCOME TO DELIVERY MS\n")

    ijobs=int(Jobs.query.filter_by(jstatus="Incomplete").count())
    manager = multiprocessing.Manager()
    incompletejobs=manager.Value("i",ijobs)

    #initialise multiprocess to check unassigned jobs
    p = multiprocessing.Process(target=worker_check_unassignedjobs, args=(incompletejobs,))
    p.start()

    #initiate listening for messages in separate process
    p2=multiprocessing.Process(target=initiate_listening())
    p2.start()