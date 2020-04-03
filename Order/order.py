from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
import pika
import json
from os import environ


app = Flask(__name__)
##app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/200cc_order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
## set dbURL=mysql+mysqlconnector://admin:password@orders-db.cvjwtqqbkq8r.ap-southeast-1.rds.amazonaws.com:3306/200cc



db = SQLAlchemy(app)
CORS(app)

## Sending order confirmation to delivery microservice
connection=pika.BlockingConnection(pika.ConnectionParameters(host="localhost",port=5672))
channel=connection.channel()
exchangename="delivery_exchange"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def send_order(order_id, address, telegram_id):
    channel.queue_declare(queue="delivery", durable=True)
    channel.queue_bind(exchange=exchangename, queue="delivery", routing_key='delivery')
    channel.basic_publish(exchange=exchangename, routing_key="delivery", body=json.dumps(["order",[order_id,address, telegram_id]]),
        properties=pika.BasicProperties(delivery_mode=2))

channel.queue_declare(queue="order", durable=True)
channel.queue_bind(exchange=exchangename, queue="order", routing_key='order')
channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)
channel.start_consuming()

 
class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    telegram_id = db.Column(db.Integer)
    email = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
    address = db.Column(db.String(200))
    phone = db.Column(db.Integer)
    postalCode = db.Column(db.Integer)

# class Transactions(db.Model):
#     __tablename__ = 'transactions'
#     tran_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
#     order_id = db.Column(db.Integer, ForeignKey('Order.order_id'))
#     quantity = db.Column(db.Integer)
#     price = db.Column(db.Integer)
#     amount = db.Column(db.Integer)
#     ##time = db.Column(datetime.now())

 
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

        ##last_item = Order.query.order_by(Order.order_id.desc()).first()
        ##print(last_item)
        
        send_order(orderid, data["address"], data["telegram_id"]) ## Send order to delivery microservice


    except:

        ## Don't know why it is triggering this even though it is successful
        return data, 500
 
    return jsonify({"Order has been created!"}), 201

if __name__ == '__main__':
    ##app.run(port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
