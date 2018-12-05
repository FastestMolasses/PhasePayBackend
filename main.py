import os
import json

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from math import radians, cos, sin, asin, sqrt
from flask import Flask, request, jsonify, Response

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

orders = []


@app.route('/send_order', methods=['POST'])
def send_order():
    j = json.loads(request.data)

    if not j.get('storeName') or not j.get('spent') or not j.get('id'):
        return "storeName AND spent AND id REQUIRED", 400

    orders.append(j)
    
    return "OK", 200


@app.route('/get_orders', methods=['GET'])
def get_orders():
    """
        Returns all the orders for the user.

        Usage:
        - Make a get request to endpoint /get_orders
        - Include user ID as parameter id

        Example URI:
            /get_orders?id=019239
    """
    return Response(json.dumps(str(orders)), mimetype='application/json')


if __name__ == '__main__':
    app.run()
