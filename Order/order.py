from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
import pika
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/200cc_order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

## Connection details
hostname = "localhost"
port = 5672

## Sending order confirmation to delivery microservice
connection=pika.BlockingConnection(pika.ConnectionParameters(host="localhost",port=5672))
channel=connection.channel()
exchangename="delivery_exchange"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

def send_order(order_id, address, telegram_id):
    channel.queue_declare(queue="delivery", durable=True)
    channel.queue_bind(exchange=exchangename, queue="delivery", routing_key='delivery')
    channel.basic_publish(exchange=exchangename, routing_key="delivery", body=json.dumps(["order",[order_id,address, telegram_id]]),
        properties=pika.BasicProperties(delivery_mode=2))
    print("Order " + order_id + " was sent")

 
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


    def __init__(self, telegram_id, name, email, quantity, address, phone, postalCode):
        self.telegram_id = telegram_id
        self.name = name
        self.email = email
        self.quantity = quantity
        self.address = address 
        self.phone = phone
        self.postalCode = postalCode

 
    def json(self):
        return {"order_id": self.order_id, "telegram_id": self.telegram_id, "name": self.name, "quantity": self.quantity, "address": self.address, "phone": self.phone, "postalCode": self.postalCode}

@app.route("/order", methods=['POST'])
def add_order():


    data = request.get_json()
    order = Order(**data)
    
    try:

        db.session.add(order)
        db.session.commit()
        
        orderid = Order.query.order_by(Order.order_id.desc()).first().order_id

        ##last_item = Order.query.order_by(Order.order_id.desc()).first()
        ##print(last_item)
        
        send_order(orderid, data["address"], data["telegram_id"]) ## Send order to delivery microservice


    except:
        return jsonify(order.json()), 500
 
    return jsonify({"Order has been created!"}), 201

if __name__ == '__main__':
    app.run(port=5001, debug=True)