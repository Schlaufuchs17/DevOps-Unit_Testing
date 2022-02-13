from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Bienvenido!"}

def test_buscar():
    response = client.get("/consulta?string=consola")
    assert response.status_code == 200
    assert response.json() == {"Numero": 0}

def test_add():
    response = client.post("/almacena?string=Videojuego")
    assert response.status_code == 200
    assert response.json() == {"Añadido correctamente"}

def test_buscar_servicio():
    response = client.get("/consulta?string=servicio")
    assert response.status_code == 200
    assert response.json() == {"Numero": 1}

def test_insertar_acento():
    response = client.post("/almacena?string=periférico")
    assert response.status_code == 200
    assert response.json() == {"Añadido correctamente"}

def test_buscar_acento(): # Si es correcto deberia devolver 0
    response = client.get("/consulta?string=periférico")
    assert response.status_code == 200
    assert response.json() == {"Numero" : 0}

def test_insertar_mayusculas():
    response = client.post("/almacena?string=RESERVA")
    assert response.status_code == 200
    assert response.json() == {"Añadido correctamente"}

def test_buscar_mayusculas(): # Si es correcto deberia devolver 0
    response = client.get("/consulta?string=RESERVA")
    assert response.status_code == 200
    assert response.json() == {"Numero" : 0}