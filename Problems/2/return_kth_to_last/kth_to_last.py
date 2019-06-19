#!/usr/bin/env python3


from singly_linked_list import Node, SinglyLinkedList


"""
Retrun Kth to Last: Implement an alogirightm to find the kth to last element
of a singly linked list.
"""


def kth_to_last(lst, k):
    """
    This solution implies that the singly linked list implemented with the
    size variable.
    """
    if k < 0 or k > lst.size - 1:
        return None
    n = lst.size - k - 1
    node = lst.head
    for i in range(n):
        node = node.next
    return node


def kth_to_last_alt(lst, k):
    """
    This solution implies that the singly linked list implemented without the
    size variable.
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
