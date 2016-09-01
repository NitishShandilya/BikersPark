"""
Given an array of n distinct integers sorted in ascending order,
write a function that returns a Fixed Point in the array,
if there is any Fixed Point present in array, else returns -1.
Fixed Point in an array is an index i such that arr[i] is equal to i.
Note that integers in array can be negative.
"""
import math
class FixedPointInArray(object):
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

    def findFixedPoint(self):
        low = 0
        high = self.length-1

        while low<=high:
            mid = low + int(math.ceil((high-low)/2))
            if mid == self.arr[mid]:
                return mid
            elif mid > self.arr[mid]:
                low = mid+1
            else:
                high = mid-1
        return -1

arr = [-10,-8,-4,-2,0,5,8,9]
fixedPoint = FixedPointInArray(arr)
f = fixedPoint.findFixedPoint()
if  f == -1:
    print "No fixed point found"
else:
    print "Fixed point found at " + str(f)