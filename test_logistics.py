from mylib.logistics import CITIES, distance_between_two_points, cities_list
from main import app
from fastapi.testclient import TestClient
import pytest

def test_distance_between_two_points():
    assert (
        distance_between_two_points(CITIES[0][1], CITIES[1][1])
    ) == 7227.494205942177


def test_cities_list():
    assert "New York" in cities_list()


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Logistics INC"}