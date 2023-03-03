import pytest
from greedy.minimum_operations import minimum_operations


def test_example_one():
    # Arrange
    nums = [1, 1, 1]

    # Act
    answer = minimum_operations(nums)

    # Assert
    assert answer == 3


def test_example_two():
    # Arrange
    nums = [1, 5, 2, 4, 1]
    # Act
    answer = minimum_operations(nums)

    # Assert
    assert answer == 14


def test_example_three():
    # Arrange
    nums = [8]

    # Act
    answer = minimum_operations(nums)

    # Assert
    assert answer == 0
