import pytest
from app import app, db
from app.models.animal import Animal

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for the root endpoint
def test_database_connection():
    with app.app_context():
        db.create_all()
        assert db.engine.url.database == 'postgres'

# Test for Animal Model

# This Animal Model test for response status code 200 means that the request was successful
def test_get_animals(client):
    with app.app_context():
        response = client.get('/animal/')
        assert response.status_code == 200

# Test for Employee Model
        
# This Employee Model test for response status code 200 means that the request was successful
def test_get_employees(client):
    with app.app_context():
        response = client.get('/employee/')
        assert response.status_code == 200
