import requests

BASE_URL = "http://52.4.70.65:5000"


def test_health_endpoint():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_prediction_endpoint():
    payload = {"feature1": 2, "feature2": 3}
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["prediction"] == 13
