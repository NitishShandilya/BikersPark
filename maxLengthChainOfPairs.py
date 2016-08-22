"""
Given n pairs of numbers. In every pair, the first number is always smaller than the second number.
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion.
Find the longest chain which can be formed from a given set of pairs.
The program assumes that the array is sorted in increasing order and the elements in the array comes in pairs,
that is element i and i+1 are always pairs.
"""
class Wrapper(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

class MaxLengthChainOfPairs(object):
    def __init__(self,arr):
        self.arr = arr
        self.listPairs = []
        self.length = len(self.arr)/2
        self.dpArray = [1] * self.length
        for i in range(0,len(self.arr),2):
            wrapper = Wrapper(self.arr[i], self.arr[i+1])
            self.listPairs.append(wrapper)

    def findLength(self):
        for i in range(0, self.length):
            for j in range(0, i):
                if self.listPairs[j].b < self.listPairs[i].a:
                    self.dpArray[i] = max(self.dpArray[i], self.dpArray[j] + 1)

        maxLength = 0
        for i in range(0, len(self.dpArray)):
            if self.dpArray[i] > maxLength:
                maxLength = self.dpArray[i]

        return maxLength


arr = [5,24,15,28,27,40,39,60,50,90]
longest = MaxLengthChainOfPairs(arr)
print longest.findLength()

