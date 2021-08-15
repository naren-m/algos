import context

import unittest

from data_structures.dynamic_arrays import DynamicArray


class DynamicArrays(unittest.TestCase):
    def test__init(self):
        array = DynamicArray()
        for i in range(0,4):
            array.pushback(i)

        self.assertEqual(array.size, 4)
        self.assertEqual(array.capacity, 4)

    def test_pushback(self):
        array = DynamicArray()

        for i in range(0, 10):
            array.pushback(i)

        self.assertEqual(array.size, 10)
        self.assertEqual(array.capacity, 16)

    def test_remove(self):
        array = DynamicArray()

        for i in range(0, 10):
            array.pushback(i)

        self.assertEqual(array.size, 10)
        self.assertEqual(array.capacity, 16)

        array.remove(4)
        self.assertEqual(str(array), '[0, 1, 2, 3, 5, 6, 7, 8, 9,]')

        array.remove(4)
        self.assertEqual(str(array), '[0, 1, 2, 3, 6, 7, 8, 9,]')

        array.remove(0)
        self.assertEqual(str(array), '[1, 2, 3, 6, 7, 8, 9,]')

        array.remove(6)
        self.assertEqual(str(array), '[1, 2, 3, 6, 7, 8,]')