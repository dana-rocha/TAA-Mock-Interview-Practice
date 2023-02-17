import pytest
from Has_Cycle.cycle_linked_list import has_cycle, ListNode


def test_example_one():
    # Arrange
    node_0 = ListNode(3)
    node_1 = ListNode(2)
    node_2 = ListNode(0)
    node_3 = ListNode(-4)

    node_0.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_1

    # Act
    answer = has_cycle(node_0)

    # Assert
    assert answer


def test_example_two():
    # Arrange
    node_0 = ListNode(1)
    node_1 = ListNode(2)

    node_0.next = node_1
    node_1.next = node_0

    # Act
    answer = has_cycle(node_0)

    # Assert
    assert answer


def test_empty_list():
    # Arrange
    list_1 = None

    # Act
    answer = has_cycle(list_1)

    # Assert
    assert not answer


def test_one_element_list():
    # Arrange
    list_1 = ListNode(1)

    # Act
    answer = has_cycle(list_1)

    # Assert
    assert not answer


def test_no_cycles():

    #Arrange
    node_0 = ListNode(3)
    node_1 = ListNode(2)
    node_2 = ListNode(0)
    node_3 = ListNode(-4)

    node_0.next = node_1
    node_1.next = node_2
    node_2.next = node_3

    #Act
    answer = has_cycle(node_0)

    #Assert
    assert not answer


def test_duplicate_values_but_not_references_return_false():
    #Arrange
    node_0 = ListNode(3)
    node_1 = ListNode(2)
    node_2 = ListNode(0)
    node_3 = ListNode(-4)
    node_4 = ListNode(2)

    node_0.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    #Act
    answer = has_cycle(node_0)

    #Assert
    assert not answer
