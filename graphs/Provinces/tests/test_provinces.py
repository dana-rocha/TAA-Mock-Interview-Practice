import pytest
from graphs.Provinces import num_provinces


def test_example_one_returns_two():
    is_connected = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

    result = num_provinces(is_connected)

    assert result == 2


def test_example_two_returns_two():
    is_connected = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]

    result = num_provinces(is_connected)

    assert result == 2


def test_example_three_returns_three():
    is_connected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    result = num_provinces(is_connected)

    assert result == 3


def test_empty_graph_returns_zero():
    is_connected = []

    result = num_provinces(is_connected)

    assert result == 0


def test_one_node_graph_returns_one():
    is_connected = [[0]]

    result = num_provinces(is_connected)

    assert result == 1


def test_fully_connected_graph_returns_one():
    is_connected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    result = num_provinces(is_connected)

    assert result == 1


def test_graph_with_cycle():
    is_connected = [[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]

    result = num_provinces(is_connected)

    assert result == 2
