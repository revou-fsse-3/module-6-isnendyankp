from flask import Flask
from app.route import pokemon_route, customer_route , animal_route
import os
from app.utils.database import db

app = Flask(__name__)

DATABASE_TYPE = os.getenv("DATABASE_TYPE")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# initialize the database alchemy
db.init_app(app)

# register the blueprints
app.register_blueprint(pokemon_route.pokemon_blueprint, url_prefix="/pokemons")
app.register_blueprint(customer_route.customer_blueprint, url_prefix="/customer")
app.register_blueprint(animal_route.animal_blueprint, url_prefix="/animal")