import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_calculate_valid():
    response = client.post("/calculate", json={
        "date": "31.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 6
    })
    
    assert response.status_code == 200
    assert response.json() == {
        "31.01.2021": 10050.0,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75
    }

def test_calculate_invalid_date():
    response = client.post("/calculate", json={
        "date": "2021-01-31",
        "periods": 3,
        "amount": 10000,
        "rate": 6
    })
    
    assert response.status_code == 422

def test_calculate_invalid_periods():
    response = client.post("/calculate", json={
        "date": "31.01.2021",
        "periods": 0,
        "amount": 10000,
        "rate": 6
    })
    
    assert response.status_code == 422

def test_calculate_invalid_amount():
    response = client.post("/calculate", json={
        "date": "31.01.2021",
        "periods": 3,
        "amount": 9999,
        "rate": 6
    })
    
    assert response.status_code == 422

def test_calculate_invalid_rate():
    response = client.post("/calculate", json={
        "date": "31.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 0
    })
    
    assert response.status_code == 422
