#### ORDER SIMULATION ####
# this is just a temporary simulation!!!

import pika
import json
import time
import random

orderaddresses=["1 Esplanade Dr, Singapore 038981", "Orchard Road, Singapore 238823", "38 Oxley Road, Singapore 238629"]

hostname="localhost"
port=5672
connection=pika.BlockingConnection(pika.ConnectionParameters(host=hostname,port=port))
channel=connection.channel()
exchangename="delivery_exchange"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

def trigger_order(): #temporary function to trigger order
    ordernumber = random.randint(0,2147483640)
    orderaddress= orderaddresses[random.randint(0,2)]
    send_order(ordernumber, orderaddress)

def send_order(ordernumber, address):
    channel.queue_declare(queue="delivery", durable=True)
    channel.queue_bind(exchange=exchangename, queue="delivery", routing_key='delivery')
    channel.basic_publish(exchange=exchangename, routing_key="delivery", body=json.dumps(["order",[ordernumber,address]]),
        properties=pika.BasicProperties(delivery_mode=2))
    print("order", ordernumber, ":", address, "sent")

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("ORDER SIMULATION")
    #temporary code to trigger order arrival
    while True:
        trigger_order()
        time.sleep(30)
    #end temporary code