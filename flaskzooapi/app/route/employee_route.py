from flask import Blueprint, jsonify, request

employee_blueprint = Blueprint('employee_endpoint', __name__)

# data array for the employees
# data such as id, name, email, phone, role, schedule
employees = [
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
        'schedule': 'Senin - Jumat'
    },
    {
        'id': 3,
        'name': 'Cindy',
        'email': 'cindy@gmail.com',
        'phone': '08123456787',
        'role': 'Manager',
        'schedule': 'Senin - Sabtu'
    }
]

# Method GET retrieve all employees in zoo
@employee_blueprint.route("/", methods=["GET"])
def get_employees():
    return jsonify(employees)

# Method GET retrieve employee by id
@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
def get_employee_by_id(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            return jsonify(employee)
    return jsonify(error='Employee not found'), 404

# Method POST add new employee to the zoo.
# The request body should be in JSON format, such as: name, email, role & schedule.
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
    
    # Generate a new employee id (assuming id is auto-incremented)
    employee_id = max([employee['id'] for employee in employees]) + 1

    # Create a new employee object
    new_employee = {
        'id': employee_id,
        'name': name,
        'email': email,
        'phone': phone,
        'role': role,
        'schedule': schedule
    }

    # Add the new employee to the employees list
    employees.append(new_employee)

    return jsonify(success='Employee created successfully'), 200

# Method PUT update employee by id
# Update employee by id, the request body should contain the updated details in JSON format.
@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.get_json()

    # Find the employee with the given id
    for employee in employees:
        if employee['id'] == employee_id:
            # Update the employee details
            employee.update(data)
            return jsonify(success='Employee updated successfully'), 200

    return jsonify(error='Employee not found'), 404

# Method DELETE delete employee by id
@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    # Find the employee with the given id
    for employee in employees:
        if employee['id'] == employee_id:
            # Delete the employee from the employees list
            employees.remove(employee)
            return jsonify(success='Employee deleted successfully'), 200

    return jsonify(error='Employee not found'), 404