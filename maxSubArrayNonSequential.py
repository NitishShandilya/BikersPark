"""
Given a 1D array, find the maximum sum obtained from a sub-array whose elements are non-sequential in the original array
"""
class MaxSubArrayNonSequential:
    def __init__(self, input):
        self.input = input

    def maxSubArray(self):
        #Define two pointers, inclusive and exclusive.
        #Inclusive is the maximum value including the number under consideration. May not include the number
        #Exclusive is the maximum sum excluding the number under consideration.
        inclusive = self.input[0]
        exclusive = 0
        for i in range(1,len(self.input)):
            temp = inclusive
            inclusive = max(inclusive, exclusive+self.input[i])
            exclusive = temp
        return inclusive

arr = [4,-5,6,9,-1]
m = MaxSubArrayNonSequential(arr)
print m.maxSubArray()