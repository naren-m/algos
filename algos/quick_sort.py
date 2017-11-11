def quick_sort(array):
    # Base case.
    #
    # No need to sort arrays with zero on one elements
    if len(array) < 2:
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


array = [2, 1, 5, 3, 4]

print(quick_sort(array))