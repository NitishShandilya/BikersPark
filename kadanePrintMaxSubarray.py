"""
Print the max sum sub-array using Kadane's algorithm
Time complexity is O(n), where n is the size of the array.
"""
INT_MIN = -32676
class MaximumSumSubarray(object):
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

    def findMaxSumKadane(self):
        max_sum = INT_MIN
        temp_sum = start_index = temp_start = 0
        end_index = -1
        for i in range(self.length):
            temp_sum += self.arr[i]
            if temp_sum < 0:
                temp_sum = 0
                temp_start = i+1
            elif temp_sum > max_sum:
                max_sum = temp_sum
                start_index = temp_start
                end_index = i

        # At least 1 non-negative element
        if end_index != -1:
            return max_sum, start_index, end_index

        # All negative elements
        max_sum = arr[0]
        start_index = end_index = 0
        for i in range(1, len(self.arr)):
            if self.arr[i] > max_sum:
                max_sum = self.arr[i]
                start_index = end_index = i
        return max_sum, start_index, end_index

# Test
arr = [-2,3,-2,1]
maxSumSubarray = MaximumSumSubarray(arr)
elements_returned = maxSumSubarray.findMaxSumKadane()
max_sum = elements_returned[0]
start_index = elements_returned[1]
end_index = elements_returned[2]
print "Maximum sum of " + str(max_sum) + " is achieved by selecting elements starting from array index " + \
      str(start_index) + " to array index " + str(end_index)
