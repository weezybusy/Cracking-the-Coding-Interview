#!/usr/bin/env python3


import unittest
from singly_linked_list import Node, SinglyLinkedList
from kth_to_last import kth_to_last, kth_to_last_alt, kth_to_last_recur


class TestKthToLast(unittest.TestCase):

    def test_kth_to_last(self):

        # Positive tests.

        lst = SinglyLinkedList()
        n = 4
        for i in range(n):
            lst.insert_tail(Node(i))
        for k in range(n):
            self.assertEqual(kth_to_last(lst, k).data, n - k - 1)

        # Negative tests.

        lst = SinglyLinkedList()
        n = 4
        for i in range(n):
            lst.insert_tail(Node(i))
        k = -1
        self.assertEqual(kth_to_last(lst, k), None)
        k = n
        self.assertEqual(kth_to_last(lst, k), None)


    def test_kth_to_last_alt(self):

        # Positive tests.

        lst = SinglyLinkedList()
        n = 4
        for i in range(n):
            lst.insert_tail(Node(i))
        for k in range(n):
            self.assertEqual(kth_to_last_alt(lst, k).data, n - k - 1)

        # Negative tests.

        lst = SinglyLinkedList()
        n = 4
        for i in range(n):
            lst.insert_tail(Node(i))
        k = -1
        self.assertEqual(kth_to_last_alt(lst, k), None)
        k = n
        self.assertEqual(kth_to_last_alt(lst, k), None)

    def test_kth_to_last_recur(self):

        # Positive tests.

        lst = SinglyLinkedList()
        n = 4
        for i in range(n):
            lst.insert_tail(Node(i))
        for k in range(n):
            self.assertEqual(kth_to_last_recur(lst, k).data, n - k - 1)

        # Negative tests.

        lst = SinglyLinkedList()
        n = 5
        for i in range(n):
            lst.insert_tail(Node(i))
        k = -1
        self.assertEqual(kth_to_last_recur(lst, k), None)
        k = n
        self.assertEqual(kth_to_last_recur(lst, k), None)


if __name__ == '__main__':
    unittest.main()
