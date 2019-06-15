#/usr/bin/env python3


import unittest
from singly_linked_list import Node, SinglyLinkedList
from remove_dups import remove_dups


class TestRemoveDups(unittest.TestCase):

    def test_remove_dups(self):

        # Check removing dups from the empty list.
        lst = SinglyLinkedList()
        remove_dups(lst)
        self.assertEqual(lst.size, 0)

        # Check removing dups from the list wiht one element in it.
        lst = SinglyLinkedList()
        lst.insert_tail(Node(1))
        remove_dups(lst)
        self.assertEqual(lst.size, 1)
        self.assertEqual(lst.head.data, 1)

        # Check removing dups from the tree with repeated element in it.
        lst = SinglyLinkedList()
        original_data = [1, 1]
        for i in range(len(original_data)):
            lst.insert_tail(Node(original_data[i]))
        remove_dups(lst)
        self.assertEqual(lst.size, 1)
        self.assertEqual(lst.head.data, 1)

        lst = SinglyLinkedList()
        original_data = [1, 1, 1, 1, 1]
        for i in range(len(original_data)):
            lst.insert_tail(Node(original_data[i]))
        remove_dups(lst)
        self.assertEqual(lst.size, 1)
        self.assertEqual(lst.head.data, 1)

        # Check removing dups from the tree with mixed data.
        lst = SinglyLinkedList()
        original_data = [1, 5, 3, 5, 4, 8, 1, 12, 33, 5]
        expected_data = [1, 5, 3, 4, 8, 12, 33]
        for i in range(len(original_data)):
            lst.insert_tail(Node(original_data[i]))
        remove_dups(lst)
        self.assertEqual(lst.size, len(expected_data))
        node = lst.head
        for i in range(len(expected_data)):
            self.assertEqual(node.data, expected_data[i])
            node = node.next

        lst = SinglyLinkedList()
        original_data = [38, 49, 51, 1080, 12, -48, -48, 1080]
        expected_data = [38, 49, 51, 1080, 12, -48]
        for i in range(len(original_data)):
            lst.insert_tail(Node(original_data[i]))
        remove_dups(lst)
        self.assertEqual(lst.size, len(expected_data))
        node = lst.head
        for i in range(len(expected_data)):
            self.assertEqual(node.data, expected_data[i])
            node = node.next

        # Check removing dups from the tree with no repeated data.
        lst = SinglyLinkedList()
        original_data = [1, 2, 3, 4, 5]
        expected_data = [1, 2, 3, 4, 5]
        for i in range(len(original_data)):
            lst.insert_tail(Node(original_data[i]))
        remove_dups(lst)
        self.assertEqual(lst.size, len(expected_data))
        node = lst.head
        for i in range(len(expected_data)):
            self.assertEqual(node.data, expected_data[i])
            node = node.next


if __name__ == '__main__':
    unittest.main()
