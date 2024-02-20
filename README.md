# Link documenation Zoo API

https://documenter.getpostman.com/view/32137747/2sA2r9V2pg


## step installer:

1. pip install poetry (global only once)
2. poetry new flaskzooapi --name app
3. cd flaskzooapi
4. python -m venv .venv
5. .venv\Scripts\activate
6. poetry config --list
7. poetry config virtualenvs.in-project true (global only once)
8. poetry add Flask
9. Flask --version
10. pip install flask
11. poetry add poetry-dotenv-plugin

## step run:
1. poetry run flask --app app run


## step for manual database setup:
1. poetry add Flask_SQLAlchemy (install flask_sqlalchemy)
2. poetry add psycopg2 (install psycopg2)