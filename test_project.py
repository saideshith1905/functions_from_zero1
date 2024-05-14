from mylib.calc import *
from calCLI import cli
from click.testing import CliRunner
import pytest


@pytest.fixture
def runner():
    return CliRunner()


# write a test command in calCLI.py
def test_add_cmd(runner):
    result = runner.invoke(cli, ["add", "1", "2"])
    assert result.exit_code == 0
    assert "3" in result.output


def test_sub_cmd(runner):
    result = runner.invoke(cli, ["sub", "1", "2"])
    assert result.exit_code == 0
    assert "-1" in result.output


def test_mul_cmd(runner):
    result = runner.invoke(cli, ["mul", "1", "2"])
    assert result.exit_code == 0
    assert "2" in result.output


def test_div_cmd(runner):
    result = runner.invoke(cli, ["div", "1", "2"])
    assert result.exit_code == 0
    assert "0.5" in result.output


def test_pow_cmd(runner):
    result = runner.invoke(cli, ["pow", "2", "2"])
    assert result.exit_code == 0
    assert "4" in result.output


def test_help(runner):
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "A calculator program" in result.output


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(1, 2) == -1


def test_mul():
    assert mul(1, 2) == 2


def test_div():
    assert div(1, 2) == 0.5


def test_pow():
    assert pow(2, 2) == 4
