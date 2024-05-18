from mylib.logistics import (
    CITIES,
    distance_between_two_points,
    cities_list,
    travel_time,
)
from main import app
from fastapi.testclient import TestClient
import pytest


def test_distance_between_two_points():
    assert (
        distance_between_two_points(CITIES[0][1], CITIES[1][1])
    ) == 7227.494205942177


# build a test for teavel_time
def test_travel_time():
    hours = travel_time("New York", "Los Angeles")
    assert hours == 120


def test_cities_list():
    assert "New York" in cities_list()


### web application testing
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Logistics INC"}


# building test for the cities endpoint
def test_cities(client):
    response = client.get("/cities")
    assert response.status_code == 200
    assert "cities" in response.json()
    assert "Dallas" in response.json()["cities"]
    assert "New York" in response.json()["cities"]
    assert "Los Angeles" in response.json()["cities"]
    assert "Chicago" in response.json()["cities"]
    assert "Houston" in response.json()["cities"]


# buid test distance for the distance endpoint
def test_distance(client):
    response = client.post(
        "/distance",
        json={"city1": {"name": "New York"}, "city2": {"name": "Los Angeles"}},
    )
    assert response.status_code == 200
    assert "distance" in response.json()
    assert response.json()["distance"] == 7227.494205942177
