#!/usr/bin/env python3


"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
"""


def remove_dups(lst):

    if lst.size < 2:
        return

    check = lst.head
    prev = lst.head
    curr = lst.head.next

    while True:
        while curr is not None:
            if curr.data == check.data:
                prev.next = curr.next
                lst.size -= 1
            else:
                prev = prev.next
            curr = curr.next
        if check.next is None:
            break
        check = check.next
        prev = check
        curr = check.next
