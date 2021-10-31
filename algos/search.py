def linear(A, k):
    for i in range(len(A)):
        if A[i] == k:
            return i

    return None


def binary(arr, val):
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


_search_algos = [linear, binary]

tests = [{
    'input': ([17, 20, 26, 31, 44, 54, 55, 77, 93], 55),
    'expected': 6,
}, {
    'input': ([2, 7, 10, 15, 18, 19, 20, 30, 36, 43, 45, 48, 50], 19),
    'expected': 5
}, {
    'input': ([2, 7, 10, 15, 18, 19, 20, 30, 36, 43, 45, 48, 50], 999),
    'expected': None
}]

for _search_algo in _search_algos:
    for test in tests:
        got = _search_algo(*test['input'])
        print('{}: Expected {}, got {}'.format(_search_algo.__name__,
                                               test['expected'], got))
        assert got == test['expected']
