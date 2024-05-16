from mylib.logistics import CITIES, distance_between_two_points, cities_list


def test_distance_between_two_points():
    assert (
        distance_between_two_points(CITIES[0][1], CITIES[1][1])
    ) == 7227.494205942177


def test_cities_list():
    assert "New York" in cities_list()
