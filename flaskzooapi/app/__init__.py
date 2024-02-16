from flask import Flask
from app.route import pokemon_route
import os

app = Flask(__name__)

DATABASE_TYPE = os.getenv("DATABASE_TYPE")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
app.config["SQLALCHEMY_DATABASE_URI"] = f""

app.register_blueprint(pokemon_route.pokemon_blueprint, url_prefix="/pokemons")