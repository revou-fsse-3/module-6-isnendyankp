from flask import Blueprint, jsonify

animal_blueprint = Blueprint('animal_endpoint', __name__)

# data array for the animals
# data such as species, age, gender, special requirements
animals = [
    {
        'id': 1,
        'species': 'Harimau',
        'age': 5,
        'gender': 'Jantan',
        'special_requirements': 'Raw meat'
    },
    {
        'id': 2,
        'species': 'Gajah',
        'age': 10,
        'gender': 'Betina',
        'special_requirements': 'Water bath'
    },
    {
        'id': 3,
        'species': 'Jerapah',
        'age': 7,
        'gender': 'Jantan',
        'special_requirements': 'High ceiling'
    }
]

# method GET: retrieve all animals in zoo
@animal_blueprint.route("/", methods=["GET"])
def get_animals():
    return jsonify(animals)

# method GET: retrieve animal by id
@animal_blueprint.route("/<int:animal_id>", methods=["GET"])
def get_animal_by_id(animal_id):
    for animal in animals:
        if animal['id'] == animal_id:
            return jsonify(animal)
    return jsonify(error='Animal not found'), 404

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