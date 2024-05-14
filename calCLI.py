#!/usr/bin/env python3

from mylib.calc import add, sub, mul, div, power
import click


@click.group()
def cli():
    """A calculator program"""


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_cmd(a, b):
    """Add two numbers
    ex:
    ./calCLI.py add 1 2"""
    # use colored o/p tp print the result
    click.secho(f"{a}+{b}= {add(a,b)}", fg="green")


@cli.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub_cmd(a, b):
    """subtract two numbers
    ex:
    ./calCLI.py sub 1 2"""
    # use colored o/p tp print the result
    click.secho(f"{a}-{b}= {sub(a,b)}", fg="green")


@cli.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul_cmd(a, b):
    """multiply two numbers
    ex:
    ./calCLI.py mul 1 2"""
    # use colored o/p tp print the result
    click.secho(f"{a}*{b}= {mul(a,b)}", fg="green")


@cli.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div_cmd(a, b):
    """divide two numbers
    ex:
    ./calCLI.py div 1 2"""
    # use colored o/p tp print the result
    click.secho(f"{a}/{b}= {div(a,b)}", fg="green")


@cli.command("power")
@click.argument("a", type=float)
@click.argument("b", type=float)
def power_cmd(a, b):
    """power of a number
    ex:
    ./calCLI.py pow 1 2"""
    # use colored o/p tp print the result
    click.secho(f"{a}**{b}= {power(a,b)}", fg="green")


if __name__ == "__main__":
    cli()
