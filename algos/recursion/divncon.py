def binSearch(arr, val):
    def search(arr, val, l, r):
        # Base case
        ## 1. Negative
        if l > r:
            return None

        ## 2. Positive case
        mid = (l + r) // 2
        if arr[mid] == val:
            return mid
        
        # Recursive step, rules to reduce all other cases to base case
        if val < arr[mid]:
            # Search in the left side of the array
            return search(arr, val, l, mid)

        return search(arr, val, mid+1, r)

    return search(arr, val, 0, len(arr)-1)

arr = list(range(0,10))
print(arr)

for _index, i in enumerate(range(0, 10)):
    print(binSearch(arr, i))
    index = binSearch(arr, i)
    assert index == _index