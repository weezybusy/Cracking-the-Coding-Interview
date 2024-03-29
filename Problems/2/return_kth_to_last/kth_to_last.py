#!/usr/bin/env python3


"""
Return Kth to Last: Implement an algorithm to find the kth to last element
of a singly linked list.
"""


from singly_linked_list import Node, SinglyLinkedList


# Time complexity:  O(n).
# Space complexity: O(1).
def kth_to_last(lst, k):
    """This solution implies that the singly linked list is implemented with
    the size variable.
    """
    if k < 0 or k > lst.size - 1:
        return None
    n = lst.size - k - 1
    node = lst.head
    for i in range(n):
        node = node.next
    return node


# Time complexity:  O(n).
# Space complexity: O(1).
def kth_to_last_alt(lst, k):
    """This solution implies that the singly linked list is implemented
    without the size variable.
    """
    node = lst.head
    size = 0
    while node is not None:
        node = node.next
        size += 1
    if k < 0 or k > lst.size - 1:
        return None
    n = size - k - 1
    node = lst.head
    for i in range(n):
        node = node.next
    return node


# Time complexity:  O(n).
# Space complexity: O(n).
def kth_to_last_recur(lst, k):
    """This is a recursive solution."""
    def fn(head, k):
        if head is None:
            return None, -1
        node, idx = fn(head.next, k)
        idx += 1
        if idx == k:
            return head, idx
        return node, idx
    return fn(lst.head, k)[0]
