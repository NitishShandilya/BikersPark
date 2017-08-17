
"""
Return minimum and maximum in an array.
You program should make minimum number of comparisons.
This algorithms compares the min max in pairs. Therefore,
the number of comparisons is n/2 and the complexity is O(n).
"""
def findMinAndMax(arr):
    arrLen = len(arr)
    if arrLen <=1:
        return "Min and max is " + str(arr[0])

    finalMax = finalMin = None

    # Compare first two elements
    if arr[0] > arr[1]:
        finalMax = arr[0]
        finalMin = arr[1]
    else:
        finalMax = arr[1]
        finalMin = arr[0]

    for i in range(2,arrLen-1,2):
        if arr[i] > arr[i+1]:
            if arr[i] > finalMax:
                finalMax = arr[i]
            if arr[i+1] < finalMin:
                finalMin = arr[i+1]
        else:
            if arr[i+1] > finalMax:
                finalMax = arr[i+1]
            if arr[i] < finalMin:
                finalMin = arr[i]

    return finalMax, finalMin

# Test
arr = [1,2,3,4,5,6,7,8]
maxAndMin = findMinAndMax(arr)
print "Maximum Element is " + str(maxAndMin[0])
print "Minimum Element is " + str(maxAndMin[1])
