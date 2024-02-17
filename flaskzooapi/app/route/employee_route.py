from flask import Blueprint, jsonify
from flask import request

employee_blueprint = Blueprint('employee_endpoint', __name__)

# data array for the employees
# data such as id, name, email, phone, role, schedule
employees = 'Daftar Employees :', [
    {
        'id': 1,
        'name': 'Budi',
        'email': 'budi@gmail.com',
        'phone': '08123456789',
        'role': 'Staff',
        'schedule': 'Senin - Jumat'
    },
    {
        'id': 2,
        'name': 'Andi',
        'email': 'andi@gmail.com',
        'phone': '08123456788',
        'role': 'Staff',
    },
    {
        'id': 3,
        'name': 'Cindy',
        'email': 'cindy@gmail.com',
        'phone': '08123456787',
        'role': 'Manager',
    }
]

# Method GET retrieve all employees in zoo
@employee_blueprint.route("/", methods=["GET"])
def get_employee():
    return jsonify(employees)

# Method GET retrieve employee by id
@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
def get_employee_by_id(employee_id):
    return str(employee_id)

# Method POST add new employee to the zoo.
# The request body should be in JSON format, such as: name, email, rolem & schedule.
@employee_blueprint.route("/", methods=["POST"])
def create_employee():
    data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    role = data.get('role')
    schedule = data.get('schedule')
    
    # Validate required fields
    if not name or not email or not phone or not role or not schedule:
        return jsonify(error='Missing required fields'), 400
    
    # Additional validation and processing logic if needed
    
    return jsonify(success='Employee created successfully'), 200


# Method PUT update employee by id
# update employee by id, the request body should be contain the updated details in JSON format.
@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.get_json()
    
    # Fetch the employee id from the request parameters or data (adjust this according to your implementation)
    employee_id = data.get('id') or request.args.get('id')
    
    # Check if employee id is provided
    if not employee_id:
        return jsonify(error='Employee id not provided'), 400
    
    # Update the employee with id (adjust this according to your implementation)
    # Additional logic to update the employee using the provided data
    
    return jsonify(success='Employee updated successfully'), 200

# Method DELETE delete employee by id
@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    employee_id = request.args.get('id')
    
    # Check if employee id is provided
    if not employee_id:
        return jsonify(error='Employee id not provided'), 400
    
    # Additional logic to delete the employee using the provided id
    
    return jsonify(success='Employee deleted successfully'), 200