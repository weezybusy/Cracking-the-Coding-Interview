#!/usr/bin/env python3


"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
"""


def remove_dups(lst):

    if lst.size < 2:
        return

    check_node = lst.head
    prev_node = lst.head
    curr_node = lst.head.next

    while check_node.next is not None:
        while curr_node is not None:
            if curr_node.data == check_node.data:
                prev_node.next = prev_node.next.next
                lst.size -= 1
            prev_node = curr_node
            curr_node = curr_node.next
        check_node = check_node.next
        prev_node = check_node
        curr_node = check_node.next
