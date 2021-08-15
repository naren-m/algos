# Dynamic array. 
# Idea: store the raddress of the dynamically allocated array and replace it with a new dynamically allocated arrya as and whe needed

# Opertions allowed on Dynamic array

# - get, set, pushback, remove, size

class DynamicArray:
    def __init__(self, size=4):
        self.capacity = size
        self.array = [None] * self.capacity

    def get(self, i):
        return self.array[i]

    def set(self, i, val):
        self.array[i] = val

    def pushback(self, i, val):
        pass