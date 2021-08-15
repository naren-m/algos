class Heap:
    def __init__(self, array: list) -> None:
        self.array = array
        self.heapsize = None

    def parent(self, i) -> int:
        return i // 2

    def left(self, i) -> int:
        return 2 * i + 1

    def right(self, i) -> int:
        return 2 * i + 2

    def build(self):
        self.heapsize = len(self.array)
        start = (len(self.array) // 2) - 1
        for i in range(start, -1, -1):
            self.heapify(i)

    def heapify(self, i) -> None:
        l = self.left(i)
        r = self.right(i)

        largest = i

        if l < self.heapsize and self.array[l] > self.array[largest]:
            largest = l

        if r < self.heapsize and self.array[r] > self.array[largest]:
            largest = r

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(largest)

        return None

    def peek(self) -> int:
        return self.array[0]

    def extract(self) -> int:
        root = self.array[0]
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.heapsize -= 1
        self.heapify(0)
        return root


tests = [{
    'input': [5, 3, 17, 10, 84, 19, 6, 22, 9],
    'expected': [84, 22, 19, 10, 3, 17, 6, 5, 9]
}, {
    'input': [16, 4, 10, 14, 7, 9, 3, 2, 8, 1],
    'expected': [16, 14, 10, 8, 7, 9, 3, 2, 4, 1 ]
}]

for test in tests:
    h = Heap(test['input'])
    h.build()
    print('Expected {}, got {}'.format(test['expected'], h.array))
    assert h.array == test['expected']