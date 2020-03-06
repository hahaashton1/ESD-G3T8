#### DELIVERY MS ####

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import pika
import json

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
    available=db.Column(db.Boolean, nullable=False)

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
        print("Driver " +driver_id+ " successfully connected.")
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

def callback(channel, method, properties, body): 
    raw_message=json.loads(body)
    key=raw_message[0]
    message=raw_message[1]
    if (key=='validate'):
        validateDriver(message)

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("WELCOME TO DELIVERY MS")
    initiate_listening()