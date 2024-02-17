from flask import Blueprint, jsonify

employee_blueprint = Blueprint('employee_endpoint', __name__)

employees = 'Daftar Employees :', [
    {
        'id': 1,
        'name': 'Budi',
        'position': 'Manager',
        'department': 'IT'
    },
    {
        'id': 2,
        'name': 'Andi',
        'position': 'Staff',
        'department': 'IT'
    },
    {
        'id': 3,
        'name': 'Cindy',
        'position': 'Manager',
        'department': 'HRD'
    }
]

# Method GET
@employee_blueprint.route("/", methods=["GET"])
def get_employee():
    return jsonify(employees)

# Method POST
@employee_blueprint.route("/", methods=["POST"])
def create_employee():
    return 'berhasil', 200

# Method PUT
@employee_blueprint.route("/", methods=["PUT"])
def update_employee():
    return 'berhasil', 200

# Method DELETE
@employee_blueprint.route("/", methods=["DELETE"])
def delete_employee():
    return 'berhasil', 200 