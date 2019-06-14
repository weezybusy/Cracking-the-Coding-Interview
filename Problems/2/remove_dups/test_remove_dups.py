#/usr/bin/env python3


import unittest
import singly_linked_list as sll
import remove_dups as rd


class TestRemoveDups(unittest.TestCase):

    def test_remove_dups(self):
        lst = sll.SinglyLinkedList()
        values = [1, 5, 3, 5, 4, 8, 1, 12, 33, 5]
        expected_result = [1, 5, 3, 4, 8, 12, 33]

        for i in range(len(values)):
            lst.insert_tail(sll.Node(values[i]))
        rd.remove_dups(lst)

        # Check sizes match.
        self.assertEqual(lst.size, len(expected_result))
        # Check values match.
        node = lst.head
        for i in range(len(expected_result)):
            self.assertEqual(node.data, expected_result[i])
            node = node.next


if __name__ == '__main__':
    unittest.main()
