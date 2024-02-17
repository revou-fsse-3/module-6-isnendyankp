from flask import Blueprint, request
from app.models.animal import Animal
from app.utils.database import db

animal_blueprint = Blueprint('animal_endpoint', __name__)


# method GET: retrieve all animals in zoo
@animal_blueprint.route("/", methods=["GET"])
def get_animals():
    try:
        # get all animals from the database
        animals = Animal.query.all()

        return [animal.as_dict() for animal in animals], 200
    except Exception as e:
        return e, 500
    

# method GET: retrieve animal by id
@animal_blueprint.route("/<int:animal_id>", methods=["GET"])
def get_animal_by_id(animal_id):
    try:
        # get the animal from the database
        animal = Animal.query.get(animal_id)
        return animal.as_dict(), 200
    except Exception as e:
        return e, 500

# method POST: add new animal to the zoo.
# The request body should be in JSON format, such as: species, age, gener & special_requirements.
@animal_blueprint.route("/", methods=["POST"])
def create_animal():
    try :
        # get data from request
        data = request.json
        # create data animal
        animals = Animal()
        # set the animal attributes
        animals.species = data['species']
        animals.age = data['age']
        animals.gender = data['gender']
        animals.special_requirements = data['special_requirements']
        # add the animal to the database
        db.session.add(animals)
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500

# method PUT: update animal data by id
# Update an existing animal by its id.
# The request body should be in JSON format, such as: species, age, gener & special_requirements.
@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    try:
        # get the animal from the database
        animal = Animal.query.get(animal_id)
        # get data from request
        data = request.json
        # set the animal attributes
        animal.species = data['species']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.special_requirements = data['special_requirements']
        # commit the changes
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500

# method DELETE: delete animal by id
# Delete an existing animal by its id.
@animal_blueprint.route("/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    try:
        # get the animal from the database
        animal = Animal.query.get(animal_id)
        # delete the animal
        db.session.delete(animal)
        db.session.commit()
        return 'berhasil', 200
    except Exception as e:
        return e, 500