"""
    A linked list is a linear collection of data elements, called nodes, each
    pointing to the next node by means of a pointer. It is a data structure
    consisting of a group of nodes which together represent a sequence.

    wiki: https://en.wikipedia.org/wiki/Linked_list

"""

from __future__ import print_function


class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        """
            Adds node to the end of linked list
            Time Complexity: O(N)
        """
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

        self.size = self.size + 1

    def delete(self, data):
        """
            Deletes a node from linked list
            Time Complexity: O(N)

            FIXME: Has bug in this implementation
            May fail if the node we are deleting is Root node
        """
        current_node = self.head

        prev = self.head
        while current_node != None:
            if current_node.data == data:
                prev.next = current_node.next
                del current_node
                self.size = self.size - 1
                return

            prev = current_node
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        print(current_node.data, "(Head) -> ", end='')
        current_node = current_node.next
        while current_node != None:
            print(current_node.data, " -> ", end='')
            current_node = current_node.next
        print("[None]")

    def search(self, data):
        """
            Search for an element in linked list
            Time Complexity: O(N)
        """
        current_node = self.head
        while current_node != None:
            if data == current_node.data:
                return current_node
            current_node = current_node.next

        return None

    def __len__(self):
        return self.size
