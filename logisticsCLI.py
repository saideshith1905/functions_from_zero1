#!/usr/bin/env python
from mylib.logistics import (
    distance_between_two_points,
    find_coordinates,
    cities_list,
    get_coordinates,
    travel_time,
)
import click


# build a click group
@click.group()
def cli():
    """tool logistics command-line tool"""


# build a click command
@cli.command("cities")
def cities():
    """
    list cities
    example :
    ./logisticsCLI.py cities
    """
    click.echo(click.style("list of cities", fg="green"))
    for city in cities_list():
        click.echo(click.style(city, fg="red"))


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """Calculate distance between two cities
    Example:
    ./logisticsCLI.py distance "New York" "Los Angeles"
    """

    click.echo(click.style("Distance between two cities", fg="green"))
    click.echo(
        click.style(
            f"{distance_between_two_points(get_coordinates(city1), get_coordinates(city2))}miles",
            fg="blue",
        )
    )


# build a click command to estate the travel time btw 2 cities by car
# assume the speed is 60 miles per hour
@cli.command("travel")
@click.argument("city1")
@click.argument("city2")
@click.option("--speed", default=60, help="speed in miles per hour")
def travel(city1, city2, speed):
    """
    Example:
    ./logisticsCLI.py travel "New York" "Los Angeles"
    """
    click.echo(click.style("travel time btw two cities", fg="green"))
    click.echo(click.style(f"{travel_time(city1, city2, speed)} hours", fg="green"))


# finding coordinates


@cli.command("coordinates")
@click.argument("city")
def coordinates(city):
    """finding coordinates of a city
    Example:
    ./logisticsCLI.py coordinates "New York"
    """

    click.echo(click.style("Distance between two cities", fg="green"))
    click.echo(
        click.style(f"coordinates of {city} are {find_coordinates(city)}", fg="blue")
    )


if __name__ == "__main__":
    cli()
