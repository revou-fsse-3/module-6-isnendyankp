from flask import Blueprint


pokemon_blueprint = Blueprint('pokemon_endpoint', __name__)

# data  array for the pokemons

pokemons = [
    {
        "id": 1,
        "name": "bulbasaur",
        "type": "grass"
    },
    {
        "id": 2,
        "name": "charmander",
        "type": "fire"
    },
]

@pokemon_blueprint.route("/", methods=["GET"])
def get_pokemon():
    return "get pokemon"

@pokemon_blueprint.route("/", methods=["POST"])
def create_pokemon():
    return "post pokemon"

@pokemon_blueprint.route("/", methods=["PUT"])
def update_pokemon():
    return "put pokemon"

@pokemon_blueprint.route("/", methods=["DELETE"])
def delete_pokemon():
    return "delete pokemon"