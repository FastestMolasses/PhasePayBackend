import json

from models import User
from main import app, db
from flask import request, Response


@app.route('/send_order', methods=['POST'])
def send_order():
    """
        Used to save receipt data for a user

        Usage:
            - Make sure the request has storeName, spent, and username variabels
            - Make a post request with the data to save it
    """
    j = json.loads(request.data)

    # Make sure we have all the required data
    if not j.get('storeName') or not j.get('spent') or not j.get('username'):
        return "storeName AND spent AND username REQUIRED", 400

    # Check if the user exists
    user = User.query.filter_by(username=j.get('username')).first()
    if not user:
        return "USER DOES NOT EXIST", 400
    
    # Save the receipt data as a string and save to database
    receipts = json.loads(user.receipts) if user.receipts else []
    receipts.append(j)
    user.receipts = str(json.dumps(receipts))
    db.session.commit()

    return "OK", 200


@app.route('/get_orders', methods=['GET'])
def get_orders():
    """
        Returns all the orders for the user.

        Usage:
        - Make a get request to endpoint /get_orders
        - Include username as parameter 

        Example URI:
            /get_orders?username=019239
    """
    # Make sure we have the proper arguments
    username = request.args.get('username')
    if not username:
        return "NO USERNAME PROVIDED", 400

    # Check if the user exists
    user = User.query.filter_by(username=username).first()
    if not user:
        return "USER DOES NOT EXIST", 400

    # Return the receipt data
    receipts = user.receipts if user.receipts else '[]'
    return Response(receipts, mimetype='application/json')
