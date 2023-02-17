from typing import Optional


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_first(old_head, node):
    if not old_head:
        return None
    node.next = old_head
    return node

def get_last_two_nodes(head):
    previous = None
    current = head

    while current.next:
        previous = current
        current = current.next

    return previous, current


def rotate_list(head: Optional[ListNode], k: int) -> ListNode:
    if not head:
        return None

    if k < 0:
        raise ValueError("k must be greater than or equal to 0")
    elif k == 0 or head.next is None:
        return head

    for i in range(k):
        new_tail, new_head = get_last_two_nodes(head)
        new_tail.next = None
        head = add_first(head, new_head)
    return head