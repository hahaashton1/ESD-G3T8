from flask import Flask, request, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
import pika
import json
import os
import time
import multiprocessing
import stripe


pub_key = 'pk_test_3OCjoxezQuwnmuEaYecZaWeb00wfwTEIaN'
secret_key = 'sk_test_WfVgaIey5IpIwZ5X21nM2Mc4001a3jgfZl'

stripe.api_key = secret_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:password@orders-db.cvjwtqqbkq8r.ap-southeast-1.rds.amazonaws.com:3306/200cc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
##app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
## set dbURL=mysql+mysqlconnector://admin:password@orders-db.cvjwtqqbkq8r.ap-southeast-1.rds.amazonaws.com:3306/200cc

db = SQLAlchemy(app)
CORS(app)

## Sending order confirmation to delivery microservice
url = os.environ.get('CLOUDAMQP_URL', 'amqp://sbxhlzzm:q42q4qSoxVcLot-eh0-7XCICIM88hjX-@hornet.rmq.cloudamqp.com/sbxhlzzm')
params = pika.URLParameters(url)
connection=pika.BlockingConnection(params)
channel=connection.channel()
exchangename="delivery_exchange"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

def send_order(order_id, address, telegram_id):
    channel.queue_declare(queue="delivery", durable=True)
    channel.queue_bind(exchange=exchangename, queue="delivery", routing_key='delivery')
    channel.basic_publish(exchange=exchangename, routing_key="delivery", body=json.dumps(["order",[order_id,address, telegram_id]]),
        properties=pika.BasicProperties(delivery_mode=2))

def receiveMsg():
    channel.queue_declare(queue="order", durable=True)
    channel.queue_bind(exchange=exchangename, queue="order", routing_key="order")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="order", on_message_callback=callback, auto_ack=True)
    channel.start_consuming() 

def callback(channel, method, properties, body):
    print(body.decode("utf-8"))

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    telegram_id = db.Column(db.Integer)
    email = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    address = db.Column(db.String(200))
    phone = db.Column(db.Integer)
    region = db.Column(db.String(200))

# class Transactions(db.Model):
#     __tablename__ = 'transactions'
#     tran_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
#     order_id = db.Column(db.Integer, ForeignKey('Order.order_id'))
#     quantity = db.Column(db.Integer)
#     price = db.Column(db.Integer)
#     amount = db.Column(db.Integer)
#     ##time = db.Column(datetime.now())

@app.route('/pay', methods=['POST'])
def pay():
    
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=19900,
        currency='usd',
        description='The Product'
    )
 
@app.route("/order", methods=['POST'])
def add_order():

    ## Get order data from UI
    data = request.get_json()
    order = Order(**data)

    ## Prepare order data to be sent to transactions DB
    ##transaction = Transactions(quantity=,price=, amount=)
    try:

        db.session.add(order)
        db.session.commit()
        
        orderid = Order.query.order_by(Order.order_id.desc()).first().order_id

        send_order(orderid, data["address"], data["telegram_id"]) ## Send order to delivery microservice
    except:
        ## Don't know why it is triggering this even though it is successful
        return "ERROR: Order cannot be created!", 500
 
    return "Order has been created!", 201

if __name__ == '__main__':

    p = multiprocessing.Process(target=receiveMsg)
    p.start()

    app.run(port=5000, debug=True)



