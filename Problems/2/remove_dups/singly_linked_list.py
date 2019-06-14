#!/usr/bin/env python3


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        if isinstance(self.data, str):
            return f'\'{self.data}\''
        else:
            return f'{self.data}'

    def __repr__(self):
        if isinstance(self.data, str):
            return f'Node(\'{self.data}\')'
        else:
            return f'Node({self.data})'


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, new_node=None):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        elif new_node is not None:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def insert_tail(self, new_node=None):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        elif new_node is not None:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def remove_head(self):
        if self.size == 0:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def remove_tail(self):
        if self.size == 0:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            node = self.head
            prev = None
            while node.next is not None:
                prev = node
                node = node.next
            if prev is not None:
                prev.next = None
                self.tail = prev;
        self.size -= 1

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def size(self):
        return self.__size

    @head.setter
    def head(self, node):
        self.__head = node

    @tail.setter
    def tail(self, node):
        self.__tail = node

    @size.setter
    def size(self, size):
        self.__size = size

    def __repr__(self):
        return 'SinglyLinkedList()'

    def __str__(self):
        if self.head is None:
            return 'SinglyLinkedList(None)'
        node = self.head
        string = ''
        while node is not None:
            string += f'{node.data}->'
            node = node.next
        return f'SinglyLinkedList({string[:-2]})'

    def __add__(self, other):
        new_list = SinglyLinkedList()
        node = self.head
        while node is not None:
            new_list.insert_tail(node)
            node = node.next
        node = other.head
        while node is not None:
            new_list.insert_tail(node)
            node = node.next
        return new_list
