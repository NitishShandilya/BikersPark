"""
Given a string and a positive integer d. Some characters may be repeated in the given string.
Rearrange characters of the given string such that the same characters become d distance away from each other.
Note that there can be many possible rearrangements, the output should be one of the possible rearrangements.
If no such arrangement is possible, that should also be reported.

Algorithm: Count frequencies of all characters and consider the most frequent character first and
place all occurrences of it as close as possible (Help of max heap). After the most frequent character is placed,
repeat the same process for remaining characters.
"""

class Node(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
    def getChar(self):
        return self.char
    def getFreq(self):
        return self.freq

class Heap(object):
    def __init__(self, arr):
        self.arr = arr
        self.arrLen = len(self.arr)

    def maxHeapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.arrLen and self.arr[left].getFreq() > self.arr[largest].getFreq():
            largest = left
        if right < self.arrLen and self.arr[right].getFreq() > self.arr[largest].getFreq():
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.maxHeapify(largest)

    def maxHeap(self):
        iterationStart = self.arrLen // 2
        iterationEnd = -1
        steps = -1
        for i in range(iterationStart, iterationEnd, steps):
            self.maxHeapify(i)

    def extractMax(self):
        if self.arrLen == 0:
            return -1
        maxElement = self.arr[0]
        self.arr[0] = self.arr[self.arrLen-1]
        self.arr.pop(self.arrLen - 1)
        self.arrLen = len(self.arr)
        self.maxHeapify(0)
        return maxElement

    def extractMaxElements(self):
        elementsList = []
        while self.arrLen != 0:
            maxElement = self.extractMax()
            if maxElement != -1:
                elementsList.append(maxElement)

        return elementsList

class Rearrange(object):
    def __init__(self, string, dist):
        self.string = list(string)
        self.stringLen = len(self.string)
        self.dist = dist

    def rearrangeWithConstDistance(self):
        freqHash = self.computeFrequencies()
        heapifiedList = self.createNodes(freqHash)
        self.nullifyString()
        return self.rearrangeCharacters(heapifiedList)

    def computeFrequencies(self):
        freqHash = {}
        for i in range(self.stringLen):
            if self.string[i] in freqHash:
                charCount = freqHash[self.string[i]]
                freqHash[self.string[i]] = charCount + 1
            else:
                freqHash[self.string[i]] = 1

        return freqHash

    def createNodes(self, freqHash):
        nodesList = []
        for char in freqHash.keys():
            freq = freqHash[char]
            node = Node(char, freq)
            nodesList.append(node)

        heap = Heap(nodesList)
        heap.maxHeap()
        maxHeapifiedList = heap.extractMaxElements()
        return maxHeapifiedList

    def nullifyString(self):
        for i in range(self.stringLen):
            self.string[i] = 'null'

    def rearrangeCharacters(self, maxHeapifiedList):
        for node in maxHeapifiedList:
            nodeChar = node.getChar()
            nodeFreq = node.getFreq()
            nextNullIndex = self.findNextNullIndex()
            for j in range(nodeFreq):
                if ((nextNullIndex + j*self.dist) < self.stringLen) and (nextNullIndex != -1):
                        self.string[nextNullIndex + j*self.dist] = nodeChar
                else:
                    return "Cannot be rearranged"

        return "".join(self.string)

    def findNextNullIndex(self):
        i = 0
        for i in range(self.stringLen):
            if self.string[i] is "null":
                return i
        return -1

# Test
string = "aabbcc"
dist = 3
rearrangeObj = Rearrange(string,dist)
print rearrangeObj.rearrangeWithConstDistance()