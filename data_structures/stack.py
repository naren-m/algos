"""
    Stack: A stack is a basic data structure that can be logically thought as
    linear structure represented by a real physical stack or pile, a structure
    where insertion and deletion of items takes place at one end called top of
    the stack. The basic concept can be illustrated by thinking of your data set
    as a stack of plates or books where you can only take the top item off the
    stack in order to remove things from it. This structure is used all
    throughout programming.

    wiki: https://en.wikibooks.org/wiki/Data_Structures/Stacks_and_Queues

"""

class Stack:
    def __init__(self):
        self.items = list()

    def push(self, data):
        """
        Add element to top of the stack.
        Time Complexity O(1)
        """
        self.items.append(data)

    def peek(self):
        """
        Return element to top of the stack.
        Time Complexity O(1)
        """
        return self.items[len(self.items)-1]

    def pop(self):
        """
        Delete element to top of the stack.
        Time Complexity O(1)
        """
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

