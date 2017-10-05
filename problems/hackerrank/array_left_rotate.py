

# Problem from hackerrank
# https://www.hackerrank.com/challenges/ctci-array-left-rotation

from __future__ import print_function


def reverse(a, start, end):
    n = len(a)
    while start < end:
        tmp = a[start]
        a[start] = a[end]
        a[end] = tmp
        start += 1
        end -= 1
    return a


def array_left_rotation(a, n, k):
    a = reverse(a, 0, k - 1)
    a = reverse(a, k, n - 1)
    a = reverse(a, 0, n - 1)
    return a


"""
Input
5 4
1 2 3 4 5
"""


n, k = list(map(int, "5 4".strip().split(' ')))
a = list(map(int, "1 2 3 4 5".strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(' '.join(map(str, answer)))

n, k = 5, 1
a = list(map(int, "1 2 3 4 5".strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(a)
print(' '.join(map(str, answer)))


large_test = True
if large_test:
    with open('data/large_array.data', 'r') as data_file:
        data = data_file.read().split('\n')
    # print data
    n, k = list(map(int, data[0].strip().split(' ')))
    a = list(map(int, data[1].strip().split(' ')))
    answer = array_left_rotation(a, n, k)
    print(' '.join(map(str, answer)))
