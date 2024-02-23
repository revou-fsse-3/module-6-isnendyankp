import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for Employee Model
        
# This Employee Model test for response status code 200 means that the request was successful
def test_get_employees(client):
    with app.app_context():
        response = client.get('/employee/')
        assert response.status_code == 200