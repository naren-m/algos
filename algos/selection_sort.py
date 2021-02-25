def selection_sort(A):
    l = len(A)
    for i in range(l - 1):
        min_index = i
        for j in range(i + 1, l):
            if A[j] < A[min_index]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]

tests = [{
    'input': [54, 26, 93, 17, 77, 31, 44, 55, 20],
    'expected': [17, 20, 26, 31, 44, 54, 55, 77, 93]
}, {
    'input': [10, 20, 15, 45, 36, 48, 7, 60, 18, 50, 2, 19, 43, 30, 55],
    'expected': [2, 7, 10, 15, 18, 19, 20, 30, 36, 43, 45, 48, 50, 55, 60]
}]

for test in tests:
    arr = test['input']
    selection_sort(arr)
    print('Expected {}, got {}'.format(test['expected'], arr))
    assert arr == test['expected']