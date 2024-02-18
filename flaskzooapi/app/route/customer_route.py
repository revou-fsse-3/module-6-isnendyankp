from flask import Blueprint, jsonify
from app.utils.database import db
from app.models.customer import Customer

customer_blueprint = Blueprint('customers_endpoint', __name__)

# Method GET retrieve all customers in zoo
@customer_blueprint.route("/", methods=["GET"])
def get_customers():
    try:
        # get all customers from the database
        customers = Customer.query.all()
        return jsonify([customer.as_dict() for customer in customers]), 200
    except Exception as e:
        return e, 500
    
# Method GET retrieve customer by id
@customer_blueprint.route("/<int:customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    try:
        # get the customer from the database
        customer = Customer.query.get(customer_id)
        return jsonify(customer.as_dict()), 200
    except Exception as e:
        return e, 500

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