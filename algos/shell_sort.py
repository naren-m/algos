def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


tests = [{
    'input': [54, 26, 93, 17, 77, 31, 44, 55, 20],
    'expected': [17, 20, 26, 31, 44, 54, 55, 77, 93]
}, {
    'input': [10, 20, 15, 45, 36, 48, 7, 60, 18, 50, 2, 19, 43, 30, 55],
    'expected': [2, 7, 10, 15, 18, 19, 20, 30, 36, 43, 45, 48, 50, 55, 60]
}]

for test in tests:
    arr = test['input']
    shellSort(arr)
    print('Expected {}, got {}'.format(test['expected'], arr))
    assert arr == test['expected']
