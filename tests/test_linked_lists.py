import context

import unittest

from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
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

        ll.insert(value=10, index=9)

        expected = list(range(0, 10))
        expected.insert(9, 10)
        self.assertEqual(ll[9], 10)

        self._checkEqual(ll, expected)

    def _checkEqual(self, ll, expected):
        n = ll.head
        for v in expected:
            self.assertEqual(v, n.data, 'expected {}, got {}'.format(v, n.data))
            n = n.next

        self.assertEqual(len(expected), len(ll), 'Length is different, expected {}, got {}'.format(len(expected), len(ll)))


    def test_set(self):
        ll = LinkedList()
        for i in range(0, 10):
            ll.append(i)

        ll[0] = 100
        self.assertEqual(ll[0], 100)

    def test_pop(self):
        ll = LinkedList()
        for i in range(0, 10):
            ll.append(i)

        expected = list(range(0, 10))


        ll.pop(9)
        expected.pop(9)
        self._checkEqual(ll, expected)

        ll.pop(3)
        expected.pop(3)

        self._checkEqual(ll, expected)


        ll.pop(7)
        expected.pop(7)
        self._checkEqual(ll, expected)

        ll.pop(0)
        expected.pop(0)
        print(expected, ll)

        self._checkEqual(ll, expected)

        print(expected, ll)


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


    def test_find(self):
        ll = LinkedList()

        for i in range(0, 10):
            ll.append(i)

        for i in range(0, 10):
            v = ll.find(i)
            self.assertIsNotNone(v)
            self.assertEqual(v.data, i, 'expected {}, got {}'.format(i, v))

    def _createLL(self, n=9):
        ll = LinkedList()

        for i in range(0, n+1):
            ll.append(i)

        return ll

    def test_peekFront(self):
        ll = self._createLL(n=9)
        for i in range(0, 10):
            self.assertEqual(ll.peekFront(), i)
            ll.pop(0)