from flask import Blueprint, jsonify, request
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

# Method POST add new customer to the zoo.
# this is the route for the customer endpoint
@customer_blueprint.route("/", methods=["POST"])
def create_customer():
    try:
        # get data from request
        data = request.json
        # create data customer
        customer = Customer()
        # set the customer attributes
        customer.name = data['name']
        customer.email = data['email']
        customer.phone_number = data['phone_number']
        # add the customer to the database
        db.session.add(customer)
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500
    
# Method PUT update customer by id
# Update customer by id, the request body should contain the updated details in JSON format.
@customer_blueprint.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    try:
        # get the customer from the database
        customer = Customer.query.get(customer_id)
        # get data from request
        data = request.json
        # set the customer attributes
        customer.name = data['name']
        customer.email = data['email']
        customer.phone_number = data['phone_number']
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500
    
# Method DELETE delete customer by id
@customer_blueprint.route("/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        # get the customer from the database
        customer = Customer.query.get(customer_id)
        # delete the customer from the database
        db.session.delete(customer)
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500