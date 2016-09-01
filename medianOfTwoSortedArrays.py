"""
There are 2 sorted arrays A and B of size n each.
Write an algorithm to find the median of the array obtained after merging the above 2 arrays
(i.e. array of length 2n). The complexity should be O(log(n))

1) Calculate the medians m1 and m2 of the input arrays ar1[]
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
"""

def median(arr, n):
    if n % 2 == 0: # If even elements
        return (arr[n/2] + arr[n/2-1])/2
    else:
        return arr[n/2]

def getMedian(arr1, arr2, n):
    if n == 1:
        return (arr1[0] + arr2[0])/2
    if n == 2:
        return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2

    #If N is greater than 2
    m1 = median(arr1, n)
    m2 = median(arr2, n)

    # If both medians are equal, then we're done
    if m1 == m2:
        return m1
    # If m1<m2, Case 4 from the above explanation
    elif m1<m2:
        if n%2 == 0: # If even elements
            return getMedian(arr1[n/2-1:], arr2, n-n/2+1)
        else:
            return getMedian(arr1[n/2:], arr2, n-n/2)
    elif m1>m2:
        if n%2 == 0: # If even elements
            return getMedian(arr1, arr2[n/2-1:], n-n/2+1)
        else:
            return getMedian(arr1, arr2[n/2:], n-n/2)


arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]
n = len(arr1)
print getMedian(arr1, arr2, n)