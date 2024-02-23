import pytest
from app.models.animal import Animal

@pytest.fixture
# Create Test for Animal Model
def test_animal_model():
    animal = Animal(species="L")
    # Access the animal variable here
    return animal

