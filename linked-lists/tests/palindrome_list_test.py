import pytest
from Palindrome_Linked_Lists.palindrome_linked_list import is_palindrome, ListNode


def test_example_one():
    # Arrange
    list_1 = ListNode(1)
    list_1 = ListNode(2, list_1)
    list_1 = ListNode(2, list_1)
    list_1 = ListNode(1, list_1)

    # Act
    answer = is_palindrome(list_1)

    # Assert
    assert answer


def test_example_two():
    # Arrange
    list_1 = ListNode(1)
    list_1 = ListNode(2, list_1)
    
    # Act
    answer = is_palindrome(list_1)

    # Assert
    assert not answer

def test_empty_list():
    # Arrange
    list_1 = None

    # Act
    answer = is_palindrome(list_1)

    # Assert
    assert answer

def test_one_element_list():
    # Arrange
    list_1 = ListNode(1)

    # Act
    answer = is_palindrome(list_1)

    # Assert
    assert answer
