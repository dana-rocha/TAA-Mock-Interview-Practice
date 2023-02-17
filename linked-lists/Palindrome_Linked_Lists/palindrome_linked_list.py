'''
https://replit.com/@adadev/linked-list-practice-section-a

https://replit.com/@adadev/linked-list-practice-section-a#tests/palindrome_list_test.py
'''

from typing import Optional


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode({self.value})"


def transform_to_doubly_linked_list(head: ListNode):
    previous = None
    current = head
    while current is not None:
        current.previous = previous
        previous = current
        current = current.next

    return previous


def is_palindrome(head: Optional[ListNode]) -> bool:
    if head is None:
        return True

    tail = transform_to_doubly_linked_list(head)

    while (head != tail):
        if head.value != tail.value:
            return False
        head = head.next
        tail = tail.previous
    
    return True
