import requests

def test_predict():
    response = requests.post("http://localhost:8501/predict", json={"feature1": 0.5, "feature2": 1.2})
    print(response.status_code)
    print(response.json())


