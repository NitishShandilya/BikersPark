import sys
"""
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome.
For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”.
Determine the fewest cuts needed for palindrome partitioning of a given string.
For example, minimum 3 cuts are needed for “ababbbabbababa”.
The three cuts are “a|babbbab|b|ababa”. If a string is palindrome, then minimum 0 cuts are needed.
If a string of length n containing all different characters, then minimum n-1 cuts are needed.
Time Complexity is n^2.
"""

class minimumPalindromePartition(object):
    def __init__(self, inputStr):
        self.arr = list(inputStr)
        self.arrLength = len(self.arr)
        self.p = [[False for i in range(self.arrLength)] for j in range(self.arrLength)]
        self.c = [None]*self.arrLength

    def findMinCuts(self):

        # Every substring of length 1 is a palindrome
        for i in range(self.arrLength):
            self.p[i][i] = True

        # L is substring length. Build the solution in bottom up manner by
        # considering all substrings of length starting from 2 to n.
        for l in range(2,self.arrLength+1):
            for j in range(self.arrLength-l+1):
                k = j+l-1 #Ending index

                # If l is 2, then we just need to compare two characters.
                # Else we need to check two corner characters and value of P[i+1][j-1]
                if l == 2:
                    self.p[j][k] = self.arr[j] == self.arr[k]
                else:
                    self.p[j][k] = (self.arr[j] == self.arr[k]) and self.p[j+1][k-1]

        for i in range(self.arrLength):
            if self.p[0][i] == True:
                self.c[i] = 0
            else:
                self.c[i] = sys.maxint
                for j in range(i):
                    if self.p[j+1][i] == True and self.c[j]+1<self.c[i]:
                        self.c[i] = self.c[j] + 1

        return self.c[self.arrLength-1]

# Test
inputStr = 'ababbbabbababa'
minPalPartition = minimumPalindromePartition(inputStr)
print minPalPartition.findMinCuts()