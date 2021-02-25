import unittest

from ..data_structures.stack import Stack


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

if __name__ == '__main__':
    unittest.main()
