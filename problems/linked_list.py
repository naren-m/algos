import context

from data_structures.linked_list import LinkedList

class Problems:

    def find_mid(self, ll):
        fast = ll.head
        slow = ll.head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

def _createLL(n=9):
    ll = LinkedList()

    for i in range(0, n):
        ll.append(i)

    return ll


def main():
    p = Problems()
    ll = _createLL()
    mid = p.find_mid(ll)
    print(mid.data)

if __name__ == "__main__":
    main()