"""This module deals with logistics and calculates distances between two points and the time it takes to travel between two points and other logistics related questions for a given speed.

For example this module can be used to calculate the distance between two cities from geopy import distance
newport_ri = (41.49008, -71.312796) cleveland_oh = (41.499498, -81.695391)
print(distance.distance(newport_ri, cleveland_oh).miles

"""

from geopy import distance

# build a list of 10 cities in the USA and their coordinates

CITIES = [
    ("New York", "40.7128", "74.0060"),
    ("Los Angeles", "34.0522", "118.2437"),
    ("Chicago", "41.8781", "87.6298"),
    ("Houston", "29.7604", "95.3698"),
    ("Philadelphia", "39.9526", "75.1652"),
    ("Phoenix", "33.4484", "112.0740"),
    ("San Antonio", "29.4241", "98.4936"),
    ("San Diego", "32.7157", "117.1611"),
    ("Dallas", "32.7767", "96.7970"),
    ("San Jose", "37.3382", "121.8863"),
]


# calculate the distance btw two points
def distance_between_two_points(point1, point2):
    """Calculating the distance btw two cities"""
    return distance.distance(point1, point2).miles




def find_coordinates(city):
    """
    Find te coordinates of a city
    """
    return city.latitude, city.longitude


# calculate the total distance btw a list of cities
def total_distance(cities):
    """
    calculate the total distance btw a list of cities
    """
    total = 0
    for i in range(len(cities) - 1):
        total += distance_between_two_points(cities[i], cities[i + 1])
        return total


# print(distance_between_two_points((41.49008, -71.312796), (41.499498, -81.695391)))
print(total_distance(CITIES))