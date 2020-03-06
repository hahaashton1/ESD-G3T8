from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/200cc_deliverypricing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Delivery_pricing(db.Model):
    __tablename__ = 'DistancePrice' 
 
    postal = db.Column(db.String(2), primary_key=True)
    price = db.Column(db.Float(precision=2), nullable=False)

 
    def __init__(self, postal, price):
        self.postal = postal
        self.price = price

 
    def json(self):
        return {"postal": self.postal, "price": self.price} 


@app.route("/delivery_pricing/<string:postal>")
def find_by_postal(postal):
    postal = postal[:2] #Retrieve the Postal Sector (1st 2 digits of 6-digit postal codes)
    delivery_pricing = Delivery_pricing.query.filter_by(postal=postal).first()
    if delivery_pricing:
        return jsonify(delivery_pricing.json())
    return jsonify({"message": "Postal not found."}), 404

if __name__ == '__main__':
    app.run(port=5002, debug=True)