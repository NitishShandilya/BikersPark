"""
Given a sorted array (sorted in non-decreasing order) of positive numbers,
find the smallest positive integer value that cannot be represented as sum of elements of any subset of given set.
Expected time complexity is O(n).
"""


def findSmallestNum(array):
    arrayLen = len(array)
    res = 1
    i=0
    while i < arrayLen and array[i] <= res:
        res += array[i]
        i += 1
    return res

array = [1, 1, 1, 1]
print findSmallestNum(array)
