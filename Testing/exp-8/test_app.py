import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.app_context():   # IMPORTANT
        app.students = []     # reset correctly

        with app.test_client() as client:
            yield client


def test_create_student(client):
    response = client.post('/students', json={"name": "Aditya"})
    assert response.status_code == 201


def test_get_students(client):
    app.students = []
    client.post('/students', json={"name": "Jasmeen"})
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.get_json()) >= 1


def test_update_student(client):
    app.students = []
    client.post('/students', json={"name": "Old"})
    response = client.put('/students/1', json={"name": "New"})
    assert response.status_code == 200
    assert response.get_json()['name'] == "New"


def test_delete_student(client):
    app.students = []
    client.post('/students', json={"name": "Delete"})
    response = client.delete('/students/1')
    assert response.status_code == 200