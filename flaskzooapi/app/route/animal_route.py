from flask import Blueprint, jsonify

animal_blueprint = Blueprint('animal_endpoint', __name__)

animals = 'Jenis-jenis Animals :', [
    {
        'id': 1,
        'name': 'Gajah',
        'jenis': 'Mamalia',
        'habitat': 'Darat'
    },
    {
        'id': 2,
        'name': 'Ikan',
        'jenis': 'Pisces',
        'habitat': 'Air'
    },
    {
        'id': 3,
        'name': 'Burung',
        'jenis': 'Aves',
        'habitat': 'Udara'
    }
]

# method GET
@animal_blueprint.route("/", methods=["GET"])
def get_animals():
    return jsonify(animals)

# method POST
@animal_blueprint.route("/", methods=["POST"])
def create_animal():
    return 'berhasil', 200

# method PUT
@animal_blueprint.route("/", methods=["PUT"])
def update_animal():
    return 'berhasil', 200

# method DELETE
@animal_blueprint.route("/", methods=["DELETE"])
def delete_animal():
    return 'berhasil', 200