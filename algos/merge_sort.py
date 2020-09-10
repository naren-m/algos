def merge_sort(A: list):
    if len(A) == 1:
        return A

    mid = (0 + len(A)) // 2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])

    A = merge(L, R, A)

    return A


def merge(L, R, A):
    l = r = i = 0
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            A[i] = L[l]
            l += 1
        else:
            A[i] = R[r]
            r += 1
        i += 1

    while l < len(L):
        A[i] = L[l]
        i += 1
        l += 1

    while r < len(R):
        A[i] = R[r]
        i += 1
        r += 1

    return A


tests = [{
    'input': [2, 1, 5, 3, 3, 3, -1, 10, 20, 4],
    'expected': [-1, 1, 2, 3, 3, 3, 4, 5, 10, 20]
}, {
    'input': [54, 26, 93, 17, 77, 31, 44, 55, 20],
    'expected': [17, 20, 26, 31, 44, 54, 55, 77, 93]
}, {
    'input': [10, 20, 15, 45, 36, 48, 7, 60, 18, 50, 2, 19, 43, 30, 55],
    'expected': [2, 7, 10, 15, 18, 19, 20, 30, 36, 43, 45, 48, 50, 55, 60]
}]

for test in tests:
    arr = test['input']
    merge_sort(arr)
    print('Expected {}, got {}'.format(test['expected'], arr))
    assert arr == test['expected']