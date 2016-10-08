"""
An implementation of Binary indexed tree or Fenwick tree.
We have an array arr[0 . . . n-1]. We should be able to
1 Find the sum of first i elements.
2 Change value of a specified element of the array arr[i] = x where 0 <= i <= n-1.
Complexity:
Construction: Time Complexity(O(nlogn)) Memory Complexity(O(n))
Find Sum: Time Complexity(O(logn))
Update : Time Complexity(O(logn))
"""

class FenwickTree(object):
    def __init__(self, array):
        self.array = array
        self.arrLen = len(self.array)
        self.fenwickTreeLength = self.arrLen + 1
        self.fenwickTree = [0] * self.fenwickTreeLength

    def buildTree(self):
        for i in range(1, self.fenwickTreeLength):
            index = i
            value = self.array[i-1]
            self.updateAtIndex(index, value)

    def updateAtIndex(self, index, value):
        while index < self.fenwickTreeLength:
            self.fenwickTree[index] += value
            index = self.getNext(index)

    def getSum(self, start, end):
        if start < 0 or end > self.arrLen:
            return "Please input a valid range"
        index = end + 1
        total = self.fenwickTree[index]

        while index > start:
            index = self.getParent(index)
            total += self.fenwickTree[index]
        return total

    def getNext(self, index):
        return index + (index & -index)

    def getParent(self, index):
        return index - (index & -index)

# Test
arr = [3,2,-1,6,5,4,-3,3,7,2,3]
fenwickTree = FenwickTree(arr)
fenwickTree.buildTree()
print fenwickTree.getSum(0,3)
fenwickTree.updateAtIndex(2,100) # Adding 100 at position 2
print fenwickTree.getSum(0,3)