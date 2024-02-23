import pytest
from app import app, db

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

