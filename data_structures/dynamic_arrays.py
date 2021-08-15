# Dynamic array. 
# Idea: store the raddress of the dynamically allocated array and replace it with a new dynamically allocated arrya as and whe needed

# Opertions allowed on Dynamic array

# - get, set, pushback, remove, size

class DynamicArray:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self._size = 0
        self.array = [None] * self.capacity
        self._increaseFactor = 2

    def get(self, i):
        return self.array[i]

    def set(self, i, val):
        self.array[i] = val

    def pushback(self, val):
        if self.capacity == self._size:
            # resize the array
            _array = [None] * (self.capacity * self._increaseFactor)
            for i in range(self.capacity):
                _array[i] = self.array[i]
            self.array = _array
            del _array

            self.capacity *= self._increaseFactor
        
        self.array[self._size] = val
        self._size +=  1

    @property
    def size(self):
        return self._size

    def remove(self, i):
        # Remove the element and adjust the array.
        while i < self._size:
            self.array[i] = self.array[i+1]
            print(i, self.array[i])
            i = i + 1
        self._size = self._size - 1

    def __str__(self):
        s = '{}, '
        out = ''
        for i in range(self._size):
            out += s.format(self.array[i])
            if i is None:
                break
        
        return '[{}]'.format(out.strip())
