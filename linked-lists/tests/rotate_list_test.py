import pytest
from Rotate_Lists.rotate_linked_list import rotate_list, ListNode


def test_example_one():
    # Arrange
    head = ListNode(5)
    head = ListNode(4, head)
    head = ListNode(3, head)
    head = ListNode(2, head)
    head = ListNode(1, head)


    # Act
    head = rotate_list(head, 2)

    # Assert
    answer = [4, 5, 1, 2, 3]
    current = head

    assert current is not None
    for num in answer:
        assert num == current.value
        current = current.next
    
    assert current is None

def test_example_two():
    # Arrange
    head = ListNode(2)
    head = ListNode(1, head)
    head = ListNode(0, head)

    # Act
    head = rotate_list(head, 4)

    # Assert
    answer = [2, 0, 1]
    current = head

    assert current is not None
    for num in answer:
        assert num == current.value
        current = current.next
    
    assert current is None

def test_rotate_empty_list():
    # Arrange
    head = None

    # Act
    head = rotate_list(head, 4)

    # Assert
    answer = []
    current = head

    assert current is None


def test_rotate_zero_times():
    # Arrange
    head = ListNode(5)
    head = ListNode(4, head)
    head = ListNode(3, head)
    head = ListNode(2, head)
    head = ListNode(1, head)


    # Act
    head = rotate_list(head, 0)

    # Assert
    answer = [1, 2, 3, 4, 5]
    current = head

    assert current is not None
    for num in answer:
        assert num == current.value
        current = current.next
    
    assert current is None

