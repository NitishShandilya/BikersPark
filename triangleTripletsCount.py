"""
Given a positive integer array, find the number of possible triangles in a given array
Time Complexity is O(n^3)
"""
def findTriangleCounts(arr):
    result = 0
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(i+1,arr_len):
            for k in range(j+1,arr_len):
                if ((arr[i]+arr[j]>arr[k]) and (arr[j]+arr[k]>arr[i]) and (arr[i]+ arr[k]>arr[j])):
                    result += 1

    return result

# Test
arr = [10, 21, 22, 100, 101, 200, 300]
print findTriangleCounts(arr)