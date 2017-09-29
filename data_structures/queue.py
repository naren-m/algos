"""
    Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, 
    a queue is open at both its ends. One end is always used to insert data (enqueue) 
    and the other is used to remove data (dequeue). Queue follows First-In-First-Out 
    methodology, i.e., the data item stored first will be accessed first.
    
    link: https://www.tutorialspoint.com/data_structures_algorithms/dsa_queue.htm
"""
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
