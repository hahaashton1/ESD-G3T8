#### DELIVERY MS ####
# 
# POST URL http://127.0.0.1:5001/getdriverinfo/<driverid> returns JSON Object {"did": <driverID>, "name": <driverName>}
# POST URL http://127.0.0.1:5001/allocatedriver/<orderid> returns JSON Object {"did": <driverID of allocated driver>}
#          it does not do anything with the orderid as yet.
#           SORRY! I GOT TO REWRITE THE ALLOCATEDDRIVER FOR TOPIC MSG, pls dont use
#
# Thats all I've done at the moment, continue it later. Feel free to use for reference.
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/200cc_delivery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Driver_Info(db.Model):
    __tablename__= 'driverinfo'

    did=db.Column(db.String(10),primary_key=True)
    dname=db.Column(db.String(40),nullable=False)
    available=db.Column(db.Boolean, nullable=False)

@app.route("/getdriverinfo/<string:driverid>", methods=['POST'])
def get_driver_information(driverid):
    this_driver=Driver_Info.query.filter(Driver_Info.did==driverid).first()
    if this_driver:
        return json.dumps({"did": this_driver.did, "name": this_driver.dname})
    else:
        return json.dumps({"error": driverid+" not found"})

@app.route("/allocatedriver/<string:orderid>", methods=['POST'])
def allocate_driver(orderid):
    driver_arr=[]
    available_drivers = Driver_Info.query.with_entities(Driver_Info.did).filter(Driver_Info.available==True)
    for i in available_drivers:
        driver_arr.append(i[0])
    if driver_arr:
        return json.dumps({"some driver here i too lazy to write"})
    else:
        return json.dumps({"error": "No driver available"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)