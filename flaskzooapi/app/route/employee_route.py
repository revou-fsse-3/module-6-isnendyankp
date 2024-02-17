from flask import Blueprint, request
from app.models.employee import Employees
from app.utils.database import db

employee_blueprint = Blueprint('employee_endpoint', __name__)


# Method GET retrieve all employees in zoo
@employee_blueprint.route("/", methods=["GET"])
def get_employees():
    try:
        # get all employees from the database
        employees = Employees.query.all()
        return [employee.as_dict() for employee in employees], 200
    except Exception as e:
        return e, 500

# Method GET retrieve employee by id
@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
def get_employee_by_id(employee_id):
    try:
        # get the employee from the database
        employee = Employees.query.get(employee_id)
        return employee.as_dict(), 200
    except Exception as e:
        return e, 500

# Method POST add new employee to the zoo.
# The request body should be in JSON format, such as: name, email, role & schedule.
@employee_blueprint.route("/", methods=["POST"])
def create_employee():
    try:
        # get data from request
        data = request.json
        # create data employee
        employee = Employees()
        # set the employee attributes
        employee.name = data['name']
        employee.email = data['email']
        employee.phone_number = data['phone_number']
        employee.role = data['role']
        employee.schedule = data['schedule']
        # add the employee to the database
        db.session.add(employee)
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500

# Method PUT update employee by id
# Update employee by id, the request body should contain the updated details in JSON format.
@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    try:
        # get the employee from the database
        employee = Employees.query.get(employee_id)
        # get data from request
        data = request.json
        # set the employee attributes
        employee.name = data['name']
        employee.email = data['email']
        employee.phone_number = data['phone_number']
        employee.role = data['role']
        employee.schedule = data['schedule']
        # commit the changes to the database
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500

# Method DELETE delete employee by id
@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    try:
        # get the employee from the database
        employee = Employees.query.get(employee_id)
        # delete the employee from the database
        db.session.delete(employee)
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500