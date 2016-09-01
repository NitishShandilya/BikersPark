"""
Given a string, find the longest possible palindromic substring.
The algorithm is solved using Dynamic Programming. Time complexity is O(n^2) and
space complexity is O(n^2). This is much better than the Brute force logic with
O(n^3) time complexity.
"""
def longestPalindromicSubString(string):
    arr = list(string)
    arr_len = len(arr)
    dpArray = [[False for i in range(arr_len)] for j in range(arr_len)]

    for i in range(arr_len):
        dpArray[i][i] = True

    maxLength = 0
    indexStart = -1
    for l in range(2,arr_len+1):
        for i in range(arr_len-l+1):
            j = i+l-1
            if arr[i] == arr[j] and dpArray[i+1][j-1] is True:
                dpArray[i][j] = True
                maxLength = l
                indexStart = i
    if maxLength != 0:
        return "substring of " + str(maxLength) + " found starting from index " + str(indexStart)
    else:
        return "No such substring found"

# Test
string = "banana"
print longestPalindromicSubString(string)
