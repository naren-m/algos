def linear(A, k):
    for i in range(len(A)):
        if A[i] == k:
            return i

    return None


def binary(A, k):
    def _binary_search(A, k, l, r):
        m = (l + r) // 2
        if A[m] == k:
            return m
        if m == l:
            return None

        if k < A[m]:
            return _binary_search(A, k, l, m)
        else:
            return _binary_search(A, k, m + 1, r)

    return _binary_search(A, k, 0, len(A) - 1)


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
