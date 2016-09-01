"""
A majority element in an array A[] of size n is an element
that appears more than n/2 times (and hence there is at most one such element).
Find the majority element.
The algorithm is Moore's voting algorithm. Time Complexity is O(n) and space
complexity is O(1).
"""
def checkIfMajority(candidate, count, arr, arr_len):
    if count == 0:
        return None

    count = 0
    for i in range(arr_len):
        if candidate == arr[i]:
            count += 1

    if (count > arr_len/2):
        return candidate
    return None

def findMajorityElement(arr):
    arr_len = len(arr)
    count = 0
    candidate = None
    for i in range(arr_len):
        if count == 0:
            candidate = arr[i]
            count = 1
        else:
            if candidate == arr[i]:
                count += 1
            else:
                count -= 1
    return checkIfMajority(candidate, count, arr, arr_len)

arr = [2,2,2,2,3,4,5,6,7,2,4,2,2]
result = findMajorityElement(arr)
if result:
    print str(result) + " is the majority element"
else:
    print "No such majority element"