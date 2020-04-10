from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:password@orders-db.cvjwtqqbkq8r.ap-southeast-1.rds.amazonaws.com:3306/cc_price'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class distancePrice(db.Model):
    __tablename__ = 'distanceprice' 
 
    
    region_name = db.Column(db.String(100), primary_key=True)
    price = db.Column(db.Float(precision=2), nullable=False)

 
    def __init__(self, region_name, price):
        self.price = price
        self.region_name = region_name

 
    def json(self):
        return { "price": self.price, "region_name": self.region_name,} 

@app.route("/delivery_pricing")
def get_all():
	return jsonify({"prices": [distancePrice.json() for distancePrice in distancePrice.query.all()]})

# print(jsonify({"prices": [distancePrice.json() for distancePrice in distancePrice.query.all()]}))

if __name__ == '__main__':
    app.run(port=5000, debug=True)