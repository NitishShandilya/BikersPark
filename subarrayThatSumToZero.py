"""
Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.
"""
class SubArrayThatSumToZero(object):
    def __init__(self,arr):
        self.arr = arr
        self.length = len(self.arr)

    def findIfAtleastOne(self):
        if self.length == 1 and self.arr[0] == 0:
            return "The single element array contains zero and hence valid"
        if self.length == 0 or (self.length == 1 and self.arr[0] !=0):
            return "No Such Subarray found"
        sumHash = {}
        sumFromBegin = 0
        sumHash[0] = -1
        for i in range(self.length):
            sumFromBegin += self.arr[i]
            if sumFromBegin in sumHash:
                startIndex = sumHash[sumFromBegin]+1
                endIndex = i
                return "Subarray found from index " + str(startIndex) + " to " + str(endIndex)
            else:
                sumHash[sumFromBegin] = i
        return "No Such Subarray found"

# Test
arr = [2, 2, 0, 1, 6]
subarraySumsToZero = SubArrayThatSumToZero(arr)
print subarraySumsToZero.findIfAtleastOne()