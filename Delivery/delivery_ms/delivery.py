#### DELIVERY MS ####

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import pika
import json
import time
import os
import multiprocessing
import atexit
import datetime
import requests
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://admin:ProfJiang@delivery1cc.cfom8s5f4cx6.us-east-1.rds.amazonaws.com:3306/delivery1cc"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# hostname = "localhost"
# port = 5672
url=os.environ.get('CLOUDAMQP_URL', 'amqp://sbxhlzzm:q42q4qSoxVcLot-eh0-7XCICIM88hjX-@hornet.rmq.cloudamqp.com/sbxhlzzm')
params = pika.URLParameters(url)

#connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
connection = pika.BlockingConnection(params)

channel = connection.channel()

exchangename="delivery_exchange"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

class Driver_Info(db.Model):
    __tablename__= 'DriverInfo'

    did=db.Column(db.String(10),primary_key=True)
    dname=db.Column(db.String(40),nullable=False)
    dstatus=db.Column(db.String(10), nullable=False)

class Jobs(db.Model):
    __tablename__= 'Jobs'
    JobID=db.Column(db.Integer, primary_key=True)
    OrderID=db.Column(db.String(20),nullable=False)
    Address=db.Column(db.String(100),nullable=False)
    did=db.Column(db.String(10),nullable=True)
    jstatus=db.Column(db.String, nullable=False) 
    telegram=db.Column(db.String, nullable=True)
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

def send_completion_to_order(message):
    channel.queue_declare(queue="order", durable=True)
    channel.queue_bind(exchange=exchangename, queue="order", routing_key="order")        
    return channel.basic_publish(exchange=exchangename, routing_key="order", body=json.dumps(message),
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
        telegram=message[2]
        # insert order to database
        newjob=Jobs(OrderID=thisorderid, Address=thisaddress, did=None, jstatus="Pending", telegram=telegram, starttime=datetime.datetime.now())
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
        #EDIT THIS
        print("Order", completed_orderid, "has been delivered by", completed_userid)
        #release driver
        Driver_Info.query.filter_by(did=completed_userid).first().dstatus="Available"
        #complete order
        thisJob=Jobs.query.filter_by(OrderID=completed_orderid).first()
        thisJob.jstatus="Completed"
        thisJob.endtime=datetime.datetime.now()
        db.session.commit()
        #notify user
        if (thisJob.telegram):
            error = telegram_bot_sendtext(thisJob.telegram, thisJob.OrderID, "Your order has been delivered!")
            print(error)
        #notify order
        msg="Message from Delivery MS: Order "+completed_orderid+" has been delivered."
        print("Completed order", completed_orderid, "has been sent to Order MS")
        # channel.queue_declare(queue="order", durable=True)
        # channel.queue_bind(exchange=exchangename, queue="order", routing_key="order")        
        # channel.basic_publish(exchange=exchangename, routing_key="order", body=json.dumps(["order_complete",[completed_orderid, "Order has been delivered!"]]),
        # properties=pika.BasicProperties(delivery_mode=2))

def worker_check_unassignedjobs(incompletejobs):
    while (True):
        ijobs=incompletejobs.value
        print("Fantasma is looking for unassigned jobs...", ijobs, "found.")
        #get order from database
        if ijobs > 0:
            undonejob=Jobs.query.filter_by(jstatus="Incomplete").first()
            thisorderid=undonejob.OrderID
            thisaddress=undonejob.Address
            print("Trying order", thisorderid, "again:", thisaddress)
            if (assign_driver_to_order(undonejob)):
                
                incompletejobs.value-=1
        time.sleep(8)

def telegram_bot_sendtext(chatID, orderid, message):
    
    bot_token = '1145625143:AAEwff0ybTjbOrWDGOOrAXaN2OOpLZIFv5A'
    bot_chatID = chatID
    bot_message = orderid + ": " + message
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

#atexit.register()


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nWELCOME TO DELIVERY MS\n")

    ijobs=int(Jobs.query.filter_by(jstatus="Incomplete").count())
    manager = multiprocessing.Manager()
    incompletejobs=manager.Value("i",ijobs)

    #initialise multiprocess to check unassigned jobs
    p = multiprocessing.Process(target=worker_check_unassignedjobs, args=(incompletejobs,))
    p.start()

    initiate_listening()