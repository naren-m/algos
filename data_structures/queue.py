"""
    Queue is an abstract data structure, somewhat similar to Stacks.
    Unlike stacks, a queue is open at both its ends. One end is always used to
    insert data (enqueue) and the other is used to remove data (dequeue).
    Queue follows First-In-First-Out methodology, i.e., the data item stored
    first will be accessed first.

    link: https://www.tutorialspoint.com/data_structures_algorithms/dsa_queue.htm
"""


class Queue:

    def __init__(self, size=100):
        self._size = size
        self._items = [None]*self._size
        self._head = 0
        self._tail = -1

    def enqueue(self, data):
        self._tail += 1
        self._items[self._tail] = data

    def peek(self):
        return self._items[self._head]

    def dequeue(self):
        if self.isEmpty():
            return None
        head = self._items[self._head]
        self._head -= 1
        return head

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items[self._head:self._tail+1])

    def __str__(self):
        if self.isEmpty():
            return 'Queue: [], Head: {}, Tail: {}'.format(
                self._head, self._tail)
        return 'Queue: {}, Head: {}, Tail: {}'.format(
            str(self._items[self._head:self._tail+1]), self._head, self._tail)

