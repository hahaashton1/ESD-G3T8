from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/200cc_inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)
 
class Inventory(db.Model):
    __tablename__ = 'Product'
 
    PID = db.Column(db.String(10), primary_key=True)
    PName = db.Column(db.String(64), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
 
    def __init__(self, PID, PName, Quantity):
        self.PID = PID
        self.PName = PName
        self.Quantity = Quantity

 
    def json(self):
        return {"PID": self.PID, "PName": self.PName, "Quantity": self.Quantity} 

@app.route("/inventory")
def get_all():
    return jsonify({"inventory": [item.json() for item in Inventory.query.all()]})
 
 
if __name__ == '__main__':
    app.run(port=5000, debug=True)

