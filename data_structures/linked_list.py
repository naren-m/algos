"""
    A linked list is a linear collection of data elements, called nodes, each
    pointing to the next node by means of a pointer. It is a data structure
    consisting of a group of nodes which together represent a sequence.

    wiki: https://en.wikipedia.org/wiki/Linked_list

"""


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return '[{}] --> {}'.format(self.data, self.next)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def __getitem__(self, index):
        h = self._moveTo(index)

        return h.data

    def __setitem__(self, index, value):
        h = self._moveTo(index)
        h.data = value

    def _moveTo(self, index):
        h = self.head
        for i in range(index):
            h = h.next

        return h

    @property
    def size(self):
        return self._size

    def append(self, data):
        self._size +=1
        if not self.head:
            self.head = Node(data)
            return

        n = Node(data)
        h = self.head
        while h.next:
            h = h.next

        h.next = n

    def insert(self, index, value):
        self._size += 1
        n = Node(value)
        h = self._moveTo(index -1)
        n.next = h.next
        h.next = n

    def find(self, value):
        h = self.head
        while h:
            if h.data == value:
                return h
            h = h.next

        return None

    def remove(self, value):
        if self._size == 0 or not self.head:
            return
        elif self._size == 1 and self.head.data == value:
            self.head = None
            self._size -= 1
            return

        h = self.head
        if h.data == value:
            self.head = h.next
            h = None
            self._size -= 1

        prev = None
        while h:
            if h.data == value:
                break
            prev = h
            h = h.next

        if not h: return
        prev.next = h.next
        self._size -= 1


    def deleteAtEnd(self):
        h = self.head

        if h is None:
            print('LL is empty')
        elif h.next is None:
            h = None
            self._size -= 1
            return

        while h.next.next:
            h = h.next

        self._size -= 1
        h.next = None

    def pop(self, index=None):

        if index > self.size:
            return

        if index is None:
            self.deleteAtEnd()
            return

        h = self._moveTo(index - 1)

        self._size -= 1
        if h is self.head:
            self.head = h.next
            return

        h.next = h.next.next

    def peekFront(self):
        if not self.head:
            return None

        return self.head.data

    def peekBack(self):
        h = self._moveTo(self.size - 1)

        return h.data

    def pushFront(self):
        pass

    def pushBack(self):
        pass

    def __len__(self):
        return self._size


    def __str__(self):
        h = self.head
        s = ''
        while h.next:
            s += '{}, '.format(h.data)
            h = h.next

        s += '{}'.format(h.data)

        return s
