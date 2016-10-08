"""
An implementation of Segment Tree with findMin query.
Can be easily extended for other operations like finMax, etc.
Construction: Time Complexity(O(n)) and Memory Complexity(O(n))
Query: Time Complexity(O(log(n)))
"""

import math
INT_MAX = 32676


class SegmentTree(object):
    def __init__(self, array):
        self.array = array
        self.arrayLength = len(array)
        self.segmentLength = self.computeSegmentLength()

    def computeSegmentLength(self):
        segmentLength = 0
        if self.isPowerOf2():  # Power of 2
            segmentLength = 2 * self.arrayLength - 1
        else:  # Not a power of two
            segmentLength = (2 ** (int(math.ceil(math.log(self.arrayLength, 2))) + 1)) - 1

        return segmentLength

    def constructTree(self):
        self.segmentArray = [INT_MAX] * self.segmentLength
        self.recursiveConstruct(0, self.arrayLength - 1, 0)

    def recursiveConstruct(self, low, high, pos):
        if low == high:
            self.segmentArray[pos] = self.array[low]
            return
        mid = (low + high) // 2
        self.recursiveConstruct(low, mid, ((2 * pos) + 1))
        self.recursiveConstruct(mid + 1, high, ((2 * pos) + 2))
        self.segmentArray[pos] = \
            min(self.segmentArray[(2 * pos) + 1], self.segmentArray[(2 * pos) + 2])

    def findMin(self, start, end):
        if start < 0 or end > self.arrayLength - 1:
            return "Index out of range"
        return self.recursiveFindMin(start, end, 0, self.arrayLength - 1, 0)

    def recursiveFindMin(self, start, end, low, high, pos):
        if start <= low and end >= high:
            return self.segmentArray[pos]
        if start > high or end < low:
            return INT_MAX
        mid = (low + high) / 2
        return min(self.recursiveFindMin(start, end, low, mid, 2 * pos + 1),
                   self.recursiveFindMin(start, end, mid + 1, high, 2 * pos + 2))

    def isPowerOf2(self):
        return (self.arrayLength & (self.arrayLength - 1)) == 0


# Test
arr = [-1, 2, 4, 0, 5]
segmentTree = SegmentTree(arr)
segmentTree.constructTree()
print segmentTree.findMin(0, 3)
