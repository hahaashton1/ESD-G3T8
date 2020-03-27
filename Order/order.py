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
 
class Order(db.Model):
    __tablename__ = 'orders'
    ##order_id = db.Column(db.Integer, primary_key = True)
    telegram_id = db.Column(db.Integer)
    email = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
    address = db.Column(db.String(200))
    phone = db.Column(db.Integer)
    postalCode = db.Column(db.Integer)

@app.route("/order", methods=['POST'])
def add_order():

    data = request.get_json()
    order = Order(**data)
    
    try:
        db.session.add(order)
        db.session.commit()
        
        send_order(str(order[0]), address[5], order[1]) ## Send order to delivery microservice
        print("This is working")
        
    except:
        return jsonify({"message": "An error occurred creating the order."}), 500
 
    return jsonify({"Order has been created!"}), 201



def send_order(order_id, address, telegram_id):
    channel.queue_declare(queue="delivery", durable=True)
    channel.queue_bind(exchange=exchangename, queue="delivery", routing_key='delivery')
    channel.basic_publish(exchange=exchangename, routing_key="delivery", body=json.dumps(["order",[order_id,address, telegram_id]]),
        properties=pika.BasicProperties(delivery_mode=2))
    print("Order " + order_id + " was sent")

if __name__ == '__main__':
    app.run(port=5000, debug=True)