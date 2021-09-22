import context

import unittest

from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def _checkEqual(self, ll, expected):
        print('Expected: {}, Got: {}'.format(expected, ll))
        n = ll.head
        for v in expected:
            self.assertEqual(v, n.data, 'expected {}, got {}'.format(v, n.data))
            n = n.next

        self.assertEqual(len(expected), len(ll), 'Length is different, expected {}, got {}'.format(len(expected), len(ll)))

    def _createLL(self, n=9):
        ll = LinkedList()

        for i in range(0, n):
            ll.append(i)

        self.assertEqual(ll.size, n)

        return ll

    def test__init__(self):
        pass

    def test_createList(self):
        ll = LinkedList()
        for i in range(0, 10):
            ll.append(i)

        self.assertEqual(ll.size, 10)
        n = ll.head

        for i in range(0, 10):
            self.assertEqual(i, n.data)
            n = n.next

    def test_insert(self):
        ll = LinkedList()
        for i in range(0, 10):
            ll.append(i)

        expected = list(range(0, 10))

        def _insert(index, val):
            ll.insert(index, val)
            expected.insert(index, val)
            print(ll)
            self.assertEqual(ll[index], val)
            self._checkEqual(ll, expected)

        _insert(9, 10)
        _insert(0, 100)
        _insert(1, 200)
        _insert(0, 101)
        _insert(ll.size, 1000)
        _insert(ll.size, 1001)

    def test_set(self):
        ll = LinkedList()
        for i in range(0, 10):
            ll.append(i)

        ll[0] = 100
        self.assertEqual(ll[0], 100)

    def test_deleteTail(self):
        n = 5
        ll = self._createLL(n)
        print(ll.head)
        expected = list(range(0, n))

        def _deleteEnd():
            print('-'*8)
            print('Deleting element at End')
            ll.deleteTail()
            expected.pop()
            self._checkEqual(ll, expected)
            print('head: {}'.format(ll.head), '\n', expected, len(expected))

        for i in range(n):
            _deleteEnd()

    def test_deleteHead(self):
        n = 5
        ll = self._createLL(n)
        print(ll.head)
        expected = list(range(0, n))

        def _deleteHead():
            print('-'*8)
            print('Deleting element at Head')
            ll.deleteHead()
            expected.pop(0)
            self._checkEqual(ll, expected)
            print('head: {}'.format(ll.head), '\n', expected, len(expected))

        for i in range(n):
            _deleteHead()

    def test_pop(self):
        n = 5
        ll = self._createLL(n)
        print(ll.head)
        expected = list(range(0, n))

        def _pop(i):
            print('-'*8)
            print('Popping element at {}'.format(i))
            ll.pop(i)
            expected.pop(i)
            self._checkEqual(ll, expected)


        _pop(4)
        _pop(3)
        _pop(0)
        _pop(1)
        _pop(0)

        # ll.pop(1)

        # print(expected, ll)

    def test_remove(self):
        ll = LinkedList()
        for i in range(0, 10):
            ll.append(i)

        expected = list(range(0, 10))
        import random
        l = list(range(0, 10))
        random.shuffle(l)
        for key in l:
            expected.remove(key)
            ll.remove(key)
            self._checkEqual(ll, expected)

        ll = LinkedList()
        ll.append(1)
        ll.remove(1)

        self.assertEqual(ll.size, 0)

    def test_find(self):
        ll = LinkedList()

        for i in range(0, 10):
            ll.append(i)

        for i in range(0, 10):
            v = ll.find(i)
            self.assertIsNotNone(v)
            self.assertEqual(v.data, i, 'expected {}, got {}'.format(i, v))

    def test_peekFront(self):
        ll = self._createLL(n=9)
        for i in range(0, 10):
            self.assertEqual(ll.peekFront(), i)
            ll.pop(0)

    def test_peekBack(self):
        ll = self._createLL(n=9)
        expected = list(range(0, 10))
        expected.reverse()
        self.assertEqual(ll.peekBack(), 9)

        print(ll, expected)
        for i in expected:
            # self.assertEqual(ll.peekBack(), i)
            ll.pop()
            print(ll)