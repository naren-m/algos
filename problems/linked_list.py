import context

import unittest

from data_structures.linked_list import LinkedList

def _createLL(n=9):
    ll = LinkedList()

    for i in range(0, n):
        ll.append(i)

    return ll

def _createFromList(l):
    ll = LinkedList()

    for i in l:
        ll.append(i)

    return ll

def _convertArr(l):
    # Create an array of the
    # required length
    arr = []
    curr = l.head

    # Traverse the Linked List and add the
    # elements to the array one by one
    while (curr != None):
        arr.append(curr.data)
        curr = curr.next

    # Print the created array
    return arr

class Problems:
    def find_mid(self, ll):
        fast = ll.head
        slow = ll.head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def lc_add_two_numbers(self, l1, l2):
        max_len = max(l1.size, l2.size)
        l1c = l1.head
        l2c = l2.head
        o = LinkedList()
        carry = 0
        for i in range(0, max_len):

            s = l1c.data + l2c.data + carry
            carry = s % 10
            s = s // 10
            o.append(s)
            print(o.head)


        return o


class TestProblems(unittest.TestCase):
    def test_find_min(self):
        p = Problems()
        ll = _createLL(n=9)
        mid = p.find_mid(ll)
        print(mid.data)
        self.assertEqual(mid.data, 4)

    def test_lc_add_two_numbers(self):
        p = Problems()
        l1 = _createFromList([2,4,3])
        l2 = _createFromList([5,6,4])
        print(l1.head, l2.head)
        o = p.lc_add_two_numbers(l1, l2)
        o = _convertArr(o)
        self.assertEqual(o, [7,0,8])
