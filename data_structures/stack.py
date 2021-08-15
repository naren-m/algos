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
    def __init__(self, size=100):
        self._size = size
        self._top = -1
        self._items = [None]*self._size

    def push(self, data):
        """
        Add element to top of the stack.
        Time Complexity O(1)
        """
        if self._top== self._size:
            raise Exception("Stack Overflow")

        self._top += 1
        self._items[self._top] = data

    def peek(self):
        """
        Return element to top of the stack.
        Time Complexity O(1)
        """
        if self.isEmpty():
            return None

        return self._items[self._top]

    def pop(self):
        """
        Delete element to top of the stack.
        Time Complexity O(1)
        """
        if self.isEmpty():
            return None

        top = self._items[self._top]
        self._top -= 1
        return top

    def size(self):
        return len(self._items)

    def isEmpty(self):
        return self._top == -1

    def __str__(self) -> str:
        if self.isEmpty():
            return 'Stack: [], top: {}'.format(self._top)
        return 'Stack: {}, top: {}'.format(str(self._items[:self._top+1]), self._top)
