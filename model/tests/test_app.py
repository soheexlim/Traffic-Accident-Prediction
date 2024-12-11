import pytest
import os
import joblib
from app import app  # Import the Flask app from app.py

@pytest.fixture
def client():
    """Set up the Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if the homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Random Forest Predictor" in response.data

def test_valid_prediction(client):
    """Test form submission with valid inputs."""
    response = client.post('/', data={
        'CRASH_HOUR': 3,
        'CITY_TOWN_NAME_ENCODED': 6,
        'TIME_OF_DAY_ENCODED': 1,
        'SPEED_LIMIT_ENCODED': 2,
        'WEATHER_SIMPLIFIED_ENCODED': 1,
        'ROAD_SURF_COND_ENCODED': 0,
        'DAY_OF_WEEK': 4,
        'IS_WEEKEND': 0,
        'IS_NIGHT': 1,
        'IS_HOLIDAY': 0,
        'IS_RUSH_HOUR': 1
    })
    assert response.status_code == 200
    assert b"Not Likely to Crash" in response.data or b"Likely to Crash" in response.data

def test_model_exists():
    """Test if the model file exists."""
    model_path = 'calibrated_rf_model.joblib'
    assert os.path.exists(model_path), "Model file is missing!"

def test_model_load():
    """Test that the model loads successfully."""
    model_path = 'calibrated_rf_model.joblib'
    model = joblib.load(model_path)
    assert model is not None
