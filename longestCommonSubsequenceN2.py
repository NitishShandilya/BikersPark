"""
Length of longest common subsequence of two strings
"""
class LongestCommonSubsequence(object):
    def __init__(self, str1, str2):
        self.arr1 = list(str1)
        self.arr2 = list(str2)
        self.lenArr1 = len(self.arr1)
        self.lenArr2 = len(self.arr2)
        self.dpArr = [[0 for i in range(self.lenArr1+1)] for j in range(self.lenArr2+1)]

    def findLength(self):
        for i in range(self.lenArr1):
            for j in range(self.lenArr2):
                if self.arr1[i] == self.arr2[j]:
                    self.dpArr[i][j] = self.dpArr[i-1][j-1] + 1
                else:
                    self.dpArr[i][j] = max(self.dpArr[i-1][j], self.dpArr[i][j-1])

        return self.dpArr[self.lenArr1-1][self.lenArr2-1]

#Test
longest = LongestCommonSubsequence('abcdaf', 'acbcf')
print longest.findLength()