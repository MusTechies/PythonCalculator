from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculate_addition(client):
    response = client.post('/calculate', data={'num1': '2', 'num2': '3', 'operation': 'add'})
    assert b'Result: 5.0' in response.data

def test_calculate_subtraction(client):
    response = client.post('/calculate', data={'num1': '5', 'num2': '3', 'operation': 'subtract'})
    assert b'Result: 2.0' in response.data

def test_calculate_multiplication(client):
    response = client.post('/calculate', data={'num1': '4', 'num2': '3', 'operation': 'multiply'})
    assert b'Result: 12.0' in response.data

def test_calculate_division(client):
    response = client.post('/calculate', data={'num1': '10', 'num2': '2', 'operation': 'divide'})
    assert b'Result: 5.0' in response.data

def test_calculate_division_by_zero(client):
    response = client.post('/calculate', data={'num1': '5', 'num2': '0', 'operation': 'divide'})
    assert b'Error: Division by zero!' in response.data
