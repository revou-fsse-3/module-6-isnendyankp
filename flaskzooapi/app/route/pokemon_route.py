from flask import Blueprint, jsonify


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
    return jsonify(pokemons)

@pokemon_blueprint.route("/", methods=["POST"])
def create_pokemon():
    return "post pokemon"

@pokemon_blueprint.route("/<int:pokemon_id>", methods=["PUT"])
def update_pokemon(pokemon_id):
    return str(pokemon_id)

@pokemon_blueprint.route("/<int:pokemon_id>", methods=["DELETE"])
def delete_pokemon(pokemon_id):
    return str(pokemon_id)