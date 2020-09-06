def linear(A, key):
    for i, e in enumerate(A):
        if e == key:
            return i


def binary(A, key):
    def _binary_search(A, l, r, k):
        mid = (l + r) // 2
        if A[mid] == k:
            return mid

        if l == mid:
            return None

            # return None
        if key < A[mid]:
            return _binary_search(A, l, mid, k)
        else:
            return _binary_search(A, mid + 1, r, k)

    i = _binary_search(A, 0, len(A) - 1, key)
    return i


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

for test in tests:
    for _search_algo in _search_algos:
        got = _search_algo(*test['input'])
        print('{}: Expected {}, got {}'.format(_search_algo.__name__,
                                               test['expected'], got))
        assert got == test['expected']
