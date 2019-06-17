#!/usr/bin/env python3


"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
"""


# Time complexity:  O(n^2).
# Space complexity: O(1).
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


# Time complexity:  O(n^2).
# Space complexity: O(1).
def remove_dups_alt(lst):

    curr = lst.head
    while curr is not None:
        runner = curr
        while runner.next is not None:
            if runner.next.data == curr.data:
                runner.next = runner.next.next
                lst.size -= 1
            else:
                runner = runner.next
        curr = curr.next
