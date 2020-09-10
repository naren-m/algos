def quick_sort(array):
    # Base case.
    #
    # No need to sort arrays with zero on one elements
    if len(array) == 1:
        return array

    # Recursive case
    #
    # Recursively call quick sort on left and right sub-arrays

    # Dumb way of choosing pivot.
    pivot = array[0]

    # Create two sub-arrays
    #   1 - with elements that are less than pivot
    #   2 - with elements that are greater than pivot
    left = [i for i in array[1:] if i <= pivot]
    right = [i for i in array[1:] if i > pivot]

    # Join left, pivot and right sub-arrays.
    return quick_sort(left) + [pivot] + quick_sort(right)


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
    quick_sort(arr)
    print('Expected {}, got {}'.format(test['expected'], arr))
    assert arr == test['expected']