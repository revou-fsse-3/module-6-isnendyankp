from flask import Blueprint, jsonify
from app.utils.database import db
from app.models.customer import Customer

customer_blueprint = Blueprint('customers_endpoint', __name__)

# this is the route for the customer endpoint
@customer_blueprint.route("/", methods=["POST"])
def create_customer():
    try:
        # create a new customer
        customer = Customer()
        # set the customer attributes
        customer.name = "John Doe"
        customer.phone = 872
        # add the customer to the database
        db.session.add(customer)
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500