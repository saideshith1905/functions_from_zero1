#!/usr/bin/env python
from mylib.logistics import distance_between_two_points,total_distance,find_coordinates,CITIES

import click

#build a click group
@click.group()
def cli():
    """tool for calulating the total distance btw a list of cities"""

#build a click command
@cli.command("total")
def total():
    """calculate the distance btw two cities"""
    print(total_distance(CITIES))

if __name__ == "__main__":
    cli()
