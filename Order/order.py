from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/200cc_order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)
 
class Order(db.Model):
    __tablename__ = 'orders'

    email = db.Column(db.String(200), primary_key = True)
    name = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
    address = db.Column(db.String(200))
    phone = db.Column(db.Integer)
    postalCode = db.Column(db.Integer)

@app.route("/order", methods=['POST'])
def add_order():

    data = request.get_json()
    order = Order(data)
    
    try:
        db.session.add(order)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the order."}), 500
 
    return jsonify({"Order has been created!"}), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)