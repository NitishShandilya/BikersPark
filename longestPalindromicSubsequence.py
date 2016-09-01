"""
Given a string s, find the length of the longest possible palindromic subsequence
The algorithm is solved using Dynamic Programming. Time complexity is O(n^2) and
space complexity is O(n^2). This is much better than the Brute force logic with
exponential time complexity.
"""
def longestPalindromicSubSequence(string):
    arr = list(string)
    arr_len = len(arr)
    dpArray = [[0 for i in range(arr_len)] for j in range(arr_len)]
    for i in range(arr_len):
        dpArray[i][i] = 1

    for l in range(2,arr_len+1):
        for i in range(arr_len-l+1):
            j = i+l-1 # Coz i is start and i+l-1 is the end
            if arr[i] == arr[j]:
                dpArray[i][j] = 2 + dpArray[i+1][j-1]
            else:
                dpArray[i][j] = max(dpArray[i+1][j], dpArray[i][j-1])
    return dpArray[0][arr_len-1]

# Test
string = "agbdba"
print longestPalindromicSubSequence(string)
