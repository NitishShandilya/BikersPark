"""
The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given
sequence such that all elements of the subsequence are sorted in increasing order.
For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}
The program's time complexity is nlogn.
"""
class LongestIncreasingSubsequence(object):
    def __init__(self, arr):
        self.arr = arr
        self.arrLength = len(self.arr)
        self.tail = [0]*self.arrLength

    def ceilIndex(self, low, high, entry):
        while (high-low)>1:
            mid = low + (high-low)/2
            if self.tail[mid] >= entry:
                high = mid
            else:
                low = mid
        return high

    def findLength(self):
        if self.arrLength == 0:
            return 0
        tailLength = 1

        self.tail[0] = self.arr[0]
        for i in range(1, self.arrLength):
            if self.arr[i] < self.tail[0]:
                self.tail[0] = self.arr[i]
            elif self.arr[i] > self.tail[tailLength-1]:
                self.tail[tailLength] = self.arr[i]
                tailLength += 1
            else:
                self.tail[self.ceilIndex(-1, tailLength-1, self.arr[i])] = self.arr[i]

        return tailLength

#Test
arr = [2, 5, 3, 7, 11, 8, 10, 13, 6]
longest = LongestIncreasingSubsequence(arr)
print "Length of longest increasing subsequence in nlogn time complexity is " + str(longest.findLength())