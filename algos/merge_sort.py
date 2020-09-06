def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    array = merge(left, right, array)

    return array


def merge(left, right, array):
    index = 0
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            array[index] = left[l]
            l += 1
        else:
            array[index] = right[r]
            r += 1
        index += 1

    while l < len(left):
        array[index] = left[l]
        index += 1
        l += 1

    while r < len(right):
        array[index] = right[r]
        index += 1
        r += 1

    return array


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
