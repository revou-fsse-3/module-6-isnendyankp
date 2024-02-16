from flask import Blueprint, jsonify

customers_blueprint = Blueprint('customers_endpoint', __name__)

# this is the route for the customer endpoint
@customers_blueprint.route("/", methods=["GET"])
def get_customers():
    return jsonify({"message": "This is the customers endpoint"})