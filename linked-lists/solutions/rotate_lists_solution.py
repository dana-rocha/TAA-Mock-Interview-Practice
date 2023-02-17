from typing import Optional


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_first(head, node):
    if not head:
        return None
    node.next = head
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
        raise ValueError("confusion")
    elif k == 0 or head.next is None:
        return head

    for i in range(k):
        new_tail, tail = get_last_two_nodes(head)

        new_tail.next = None
        head = add_first(head, tail)
    return head