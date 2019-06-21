#!/usr/bin/env python3


"""
Retrun Kth to Last: Implement an alogirightm to find the kth to last element
of a singly linked list.
"""


from singly_linked_list import Node, SinglyLinkedList


def kth_to_last(lst, k):
    """
    This solution implies that the singly linked list is implemented with the
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
    This solution implies that the singly linked list is implemented without
    the size variable.
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


def kth_to_last_recur(node, k):
    """
    This solution implies that the singly linked list is implemented without
    the size variable.
    """
    i = getk(node, k, 0)
    if i < 0:
        return None
    while i > 0:
        node = node.next
        i -= 1
    return node


def getk(node, k, i):
    if k < 0:
        return k
    elif node.next is None:
        return i - k
    else:
        return getk(node.next, k, i+1)


lst = SinglyLinkedList()
for i in range(5):
    lst.insert_tail(Node(chr(97+i)))
print(lst)
print(f'kth_to_last_recur(lst.head, -1) -> {kth_to_last_recur(lst.head, -1)}')
print(f'kth_to_last_recur(lst.head, 0) -> {kth_to_last_recur(lst.head, 0)}')
print(f'kth_to_last_recur(lst.head, 2) -> {kth_to_last_recur(lst.head, 2)}')
print(f'kth_to_last_recur(lst.head, 4) -> {kth_to_last_recur(lst.head, 4)}')
print(f'kth_to_last_recur(lst.head, 5) -> {kth_to_last_recur(lst.head, 5)}')
