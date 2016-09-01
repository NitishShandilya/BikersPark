"""
Given an unsorted array of integers (positive and negative numbers),
find all subarrays which adds to a given number K.
Time Complexity is O(n) and Space Complexity is O(n)
"""
class SubArraysThatSumToK(object):
    def __init__(self, arr, K):
        self.arr = arr
        self.length = len(self.arr)
        self.K = K

    def findAllSubArrays(self):
        sumHash = {}
        sumHash[0] = [-1]
        sumFromBegin = 0
        for i in range(self.length):
            sumFromBegin += self.arr[i]
            if (sumFromBegin-self.K) in sumHash:
                startIndices = sumHash[sumFromBegin-self.K]
                for start in startIndices:
                    print "Subarray from indices " + str(start+1) + " to " + str(i)

            indices = []
            if sumFromBegin in sumHash:
                indices = sumHash[sumFromBegin]
            indices.append(i)
            sumHash[sumFromBegin] = indices

arr = [10, 2, 22, 20, 10]
K = 24
subArrays = SubArraysThatSumToK(arr, K)
subArrays.findAllSubArrays()
