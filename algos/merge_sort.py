def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right, arr)

def merge(left, right, arr):
    l = r = i = 0

    ll = len(left)
    lr = len(right)

    while l < ll and r < lr :
        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
        i += 1

    # poplulating remaining
    while l < ll:
        arr[i] = left[l]
        i += 1
        l += 1

    while r < lr:
        arr[i] = right[r]
        i += 1
        r += 1

    return arr



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