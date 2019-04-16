from data_structures import queue


def main():
    q = queue.Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    q.print_queue()
    while not q.is_empty():
        data = q.dequeue()
        print("Dequeued", data)
        q.print_queue()


if __name__ == '__main__':
    main()
