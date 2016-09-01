"""
A sorted array is rotated at some unknown point, find the minimum element in it.
The algorithm uses Binary search concept. We have to find a point in the array that has arr[i]>arr[i+1].
This is the crossing point. If the array is sorted in increasing order. At this point we get to know that the array is rotated.
We find this, if low > mid, then the crossing element in the first half and if not, then the crossing element
will be in the second half of the array.
Another problem of finding an element in a rotated sorted array can also be done using this concept in O(logn) time
Finding an element in a rotated sorted array can also be done without using pivot. After checking for num == a[mid],
check if left < mid, then left array is sorted, check here if not, then discard this and goto the right part.. repeat the same.
"""
class MinInSortedRotatedArray(object):
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

    def findMin(self):
        low = 0
        high = self.length-1

        # Array has not been rotated
        if self.arr[low] < self.arr[high]:
            return self.arr[low]

        while low<=high:
            mid = low + ((high-low)//2)
            if self.arr[mid] > self.arr[mid+1]:
                return self.arr[mid+1]
            elif self.arr[low] > self.arr[mid]:
                high = mid-1
            else:
                low = mid+1
        return -1

# Test
arr = [2, 3, 4, 5, 6, 7, 8, 1]
minInSorted = MinInSortedRotatedArray(arr)
print minInSorted.findMin()