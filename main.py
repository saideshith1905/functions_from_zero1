from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.logistics import (
    distance_between_two_points,
    cities_list,
    get_coordinates,
    travel_time,
)
from mylib.wiki import get_wiki_keywords


app = FastAPI()


class City(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Logistics INC"}


@app.get("/cities")
async def cities():
    """List cities with get HTTP method
    Returns back a list of cities that are available to get further information about
    """
    return {"cities": cities_list()}


# build a post method to get the distance btw two cities
@app.post("/distance")
async def distance(city1: City, city2: City):
    """Calculate distance btw the two cities with POST HTTP Method
    Returns back te distance btw 2 cities in miles"""
    return {
        "distance": distance_between_two_points(
            get_coordinates(city1.name), get_coordinates(city2.name)
        )
    }


# build a post that calculate travel time btw 2 cities  by car
@app.post("/travel")
async def travel(city1: City, city2: City):
    """Estimate travel time btw 2 cities by a car with POST HTTP method
    Returns back the travel time btw 2 cities by car
    FIXME:Bug
    """

    hours = travel_time(city1.name, city2.name, speed=60)
    return {
        "time_travel": f"{hours} hours"
        # travel_time(city1.name,(city2.name),speed)
    }


@app.post("/keywords")
async def keywords(city: City):
    """Get the top 10 keywords from the content of a page with POST HTTP Method
    Returns back the top 10 keywords from the content of a page
    """
    return {"keywords": get_wiki_keywords(city.name)}


if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")
