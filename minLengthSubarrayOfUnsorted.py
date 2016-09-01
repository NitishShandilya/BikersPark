"""
Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e]
such that sorting this sub-array makes the whole array sorted.
"""
class MinLengthSubArray(object):
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

    def findMinLengthSubArray(self):
        s = e = 0
        start = 0
        for start in range(self.length-1):
            if self.arr[start+1]<self.arr[start]:
                start = start+1
                break
        if start+1 == self.length-1: # Adding one for start to account for the loop running only until n-2
            return "Complete array is sorted"
        end = 0
        for end in range(self.length-1,0,-1):
            if self.arr[end-1]>self.arr[end]:
                end = end-1
                break
        for k in range(start):
            if self.arr[k]>self.arr[start]:
                s = k
                break
        for l in range(self.length-1,end,-1):
            if self.arr[l]<self.arr[end]:
                e = l
                break
        return self.arr[s:e+1]

# Test
arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
minLengthSubArray = MinLengthSubArray(arr)
print minLengthSubArray.findMinLengthSubArray()