class Heap:
    def __init__(self, input):
        self.input = input
        self.inputSize = len(self.input)

    def maxHeapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.inputSize and self.input[left] > self.input[largest]:
            largest = left
        if right < self.inputSize and self.input[right] > self.input[largest]:
            largest = right
        if largest != i:
            self.input[i], self.input[largest] = self.input[largest], self.input[i]
            self.maxHeapify(largest)

    def maxHeap(self):
        iterationStart = self.inputSize//2
        iterationEnd = -1
        steps = -1
        for i in range(iterationStart, iterationEnd, steps):
            self.maxHeapify(i)

    def printHeap(self):
        for i in range(self.inputSize//2):
            print "Parent: " + str(self.input[i])
            if 2 * i + 1 < self.inputSize:
                print "Left Child: " + str(self.input[2 * i + 1])
            if 2 * i + 2 < self.inputSize:
                print "Right Child: " + str(self.input[2 * i + 2])

    def printMax(self):
        print "The max element is " + str(self.input[0])

    def extractMax(self):
        if self.inputSize == 0:
            print "The array is empty"
            return
        print "The max element is " + str(self.input[0])
        self.input[0] = self.input[self.inputSize-1]
        self.input.pop(self.inputSize - 1)
        self.inputSize = len(self.input)
        self.maxHeapify(0)

    def search(self, searchTerm):
        startIndex = 0
        found = self.searchForElement(startIndex, searchTerm)
        if found is True:
            return "Element found"
        return "Element not found"

    def searchForElement(self, index, searchTerm):
        if self.input[index] == searchTerm:
            return True

        # This is the main optimization, if in maxheap the parent node is only less than the search term,
        # then we don't have to traverse further
        if self.input[index] < searchTerm:
            return False
        else:
            if (2*index+1) < self.inputSize: # Traverse left sub-tree
                return self.searchForElement(2*index+1, searchTerm)
            if (2*index+2) < self.inputSize: # Traverse right sub-tree
                return self.searchForElement(2*index+2, searchTerm)
        return False

    def printSimple(self):
        print self.input

# Test Heap
input = [70,90,2,3,1]
heap = Heap(input)
heap.maxHeap()
heap.printSimple()
#heap.printMax()
print heap.search(3)
heap.printSimple()

heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.printSimple()
heap.extractMax()
heap.extractMax()
heap.extractMax()
heap.extractMax()
