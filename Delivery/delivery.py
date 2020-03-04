#### DELIVERY MS ####
# 
# POST URL http://127.0.0.1:5001/deliver/<driverid> returns JSON Object {"did": <driverID>, "name": <<driverName>}
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

@app.route("/deliver/<string:driverid>", methods=['POST'])
def get_driver(driverid):
    this_driver=Driver_Info.query.filter(Driver_Info.did==driverid).first()
    if this_driver:
        return json.dumps({"did": this_driver.did, "name": this_driver.dname})
    else:
        return "No record found"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)