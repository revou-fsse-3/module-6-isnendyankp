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

## step run:
1. poetry run flask --app app run