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


array = [2, 1, 5, 3, 3, 3, -1, 10, 20, 4]

print(merge_sort(array))
