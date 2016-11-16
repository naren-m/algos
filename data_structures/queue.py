class Queue:

    def __init__(self):
        self.items = list()

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def size(self):
        return len(self.items)

    def print_queue(self):
        for elem in self.items:
            print elem,
        print
