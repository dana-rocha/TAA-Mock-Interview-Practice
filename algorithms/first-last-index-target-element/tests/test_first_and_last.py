import pytest
from divide_and_conquer.find_first_and_last import find_first_last


def test_one():
    # Arrange
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # Act
    answer = find_first_last(nums, target)

    # Assert
    assert answer == [3, 4]


def test_two():
    # Arrange
    nums = [5, 7, 7, 8, 8, 10]
    target = 6

    # Act
    answer = find_first_last(nums, target)

    # Assert
    assert answer == [-1, -1]


def test_three():
    # Arrange
    nums = []
    target = 0

    # Act
    answer = find_first_last(nums, target)

    # Assert
    assert answer == [-1, -1]

def test_four():
    # Arrange
    nums = [5, 5, 5, 5, 5, 5]
    target = 5

    # Act
    answer = find_first_last(nums, target)

    # Assert
    assert answer == [0, 5]
