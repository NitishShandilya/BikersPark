"""
Given a 1D array, find the maximum sum obtained from a sub-array with sequential elements.
The program utilizies Kadane's algorithm.
Time complexity is O(n), where n is the size of the array.
"""
class MaximumSumSubarray(object):
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

    def findMaxSumKadane(self):
        max_curr = max_sum = self.arr[0]
        for i in range(1, self.length):
            max_curr = max(self.arr[i]+max_curr, self.arr[i])
            max_sum = max(max_sum, max_curr)
        return max_sum
#Test
arr = [-2,-3,-2,-1]
maxSumSubarray = MaximumSumSubarray(arr)
print maxSumSubarray.findMaxSumKadane()