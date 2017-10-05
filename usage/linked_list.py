import data_structures as ds


def main():
    ll = ds.linked_list.LinkedList()
    ll.add('1')
    ll.add('2')
    ll.add('3')

    ll.print_list()
    # ll.delete('3')
    # ll.print_list()

    # print("Size = ", len(ll))

    # node = ll.search('2')
    # print("Searched for ", node.data)


if __name__ == '__main__':
    main()
