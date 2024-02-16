from flask import Blueprint, jsonify
from app.utils.database import db
from app.models.customers import Customer

customers_blueprint = Blueprint('customers_endpoint', __name__)

# this is the route for the customer endpoint
@customers_blueprint.route("/", methods=["GET"])
def create_customers():
    # create a new customer
    customers = Customer()
    # set the customer attributes
    customers.name = "John Doe"
    customers.phone = "123-456-7890"
    # add the customer to the database
    db.session.add(customers)
    db.session.commit()
    return 'Customer created successfully!', 200