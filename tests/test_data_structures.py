import context

import unittest

from data_structures.stack import Stack
from data_structures.queue import Queue


class TestStack(unittest.TestCase):
    def test__init__(self):
        s = Stack()
        self.assertEqual(s._top, -1)
        assert True  # TODO: implement your test here

    def test_push(self):
        s = Stack()
        for i in range(10):
            s.push(i)
            self.assertEqual(s.peek(), i)

        # Stack Overflow
        s = Stack(size=2)
        s.push(1)
        s.push(2)
        with self.assertRaises(Exception):
            s.push(3)


    def test_pop(self):
        s = Stack()
        for i in range(11):
            s.push(i)
            self.assertEqual(s.peek(), i)
        print()
        print(s)
        for i in range(10, -1, -1):
            self.assertEqual(s.peek(), i)
            pop = s.pop()
            self.assertNotEqual(pop, s.peek())
            self.assertEqual(pop, i)
            print(s, 'pop {}'.format(i))

        self.assertIsNone(s.pop())
        print(s)

class TestQueue(unittest.TestCase):
    def test__init__(self):
        q = Queue()
        self.assertEqual(len(q), 0)

    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        print(q)
        self.assertEqual(q.peek(), 1)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        print(q)
        self.assertEqual(q.peek(), 1)

        t = q.dequeue()
        self.assertEqual(t, 1)
        print(q)
        self.assertEqual(q.peek(), 2)

        t = q.dequeue()
        self.assertEqual(t, 2)
        print(q)
        self.assertEqual(q.peek(), 3)

        t = q.dequeue()
        self.assertEqual(t, 3)
        print(q)

        self.assertEqual(len(q), 0)
        self.assertTrue(q.isEmpty())


if __name__ == '__main__':
    unittest.main()
