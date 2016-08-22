"""
The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given
sequence such that all elements of the subsequence are sorted in increasing order.
For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}
The program's time complexity is n^2.
"""
class LongestIncreasingSubsequence(object):
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)
        self.dpArray = [1]*self.length

    def findLength(self):
        for i in range(0, self.length):
            for j in range(0,i):
                if self.arr[j] < self.arr[i]:
                    self.dpArray[i] = max(self.dpArray[i], self.dpArray[j]+1)

        maxLength = 0
        for i in range(0, len(self.dpArray)):
            if self.dpArray[i] > maxLength:
                maxLength = self.dpArray[i]

        return maxLength

#Test
arr = [-1,5,6,-2,7,0,2,4,9,10,1]
longestIncreasing = LongestIncreasingSubsequence(arr)
print longestIncreasing.findLength()