"""
Given an array of integers, find length of the largest subarray with sum equals to 0.
"""
class LargestSubArrayThatSumToZero(object):
    def __init__(self,arr):
        self.arr = arr
        self.length = len(self.arr)

    def find(self):
        if self.length == 1 and self.arr[0] == 0:
            return "The single element array contains zero and hence valid"
        if self.length == 0 or (self.length == 1 and self.arr[0] !=0):
            return "No Such Subarray found"
        sumHash = {}
        sumFromBegin = 0
        sumHash[0] = -1
        maxLength = 0
        finalStart = -1
        finalEnd = -1
        for i in range(self.length):
            sumFromBegin += self.arr[i]
            if sumFromBegin in sumHash:
                startIndex = sumHash[sumFromBegin]+1
                endIndex = i
                currMax = (endIndex - startIndex) + 1
                if currMax > maxLength:
                    finalStart = startIndex
                    finalEnd = endIndex
                    maxLength = currMax
            else:
                sumHash[sumFromBegin] = i

        if maxLength == 0:
            return "No Such Subarray found"
        return "Subarray of length " + str(maxLength) + " found between " + str(finalStart) + " and " + str(finalEnd)

# Test
arr = [15, -2, 2, -8, 1, 7, 10, 23]
largestSubarraySumsToZero = LargestSubArrayThatSumToZero(arr)
print largestSubarraySumsToZero.find()