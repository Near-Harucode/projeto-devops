from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_somar():
    response = client.post("/somar", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}

def test_subtrair():
    response = client.post("/subtrair", json={"a": 5, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"resultado": 3}

def test_multiplicar():
    response = client.post("/multiplicar", json={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"resultado": 12}

def test_dividir():
    response = client.post("/dividir", json={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}

def test_divisao_por_zero():
    response = client.post("/dividir", json={"a": 10, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"erro": "Divisão por zero não é permitida"}  
