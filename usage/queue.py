import data_structures as ds


def main():
    q = ds.queue.Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    q.print_queue()
    data = q.dequeue()
    print("Dequeued", data)


if __name__ == '__main__':
    main()
