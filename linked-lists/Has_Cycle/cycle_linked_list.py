from typing import Optional


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode({self.value})"


def has_cycle(head: Optional[ListNode]) -> bool:
    pass
