"""
Given an array arr[0...n-1] with n elements and each of the value in the array is from 1 to n,
find the occurences of all the elements in O(n) time complexity and O(1) memory complexity
"""
class FrequenciesOfElementsInPlace(object):
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

    def findFrequencies(self):
        maxEle = self.length

        for i in range(self.length):
            self.arr[i] -= 1

        for i in range(self.length):
            self.arr[self.arr[i]%maxEle] += maxEle

        for i in range(self.length):
            occurence = self.arr[i] / maxEle
            if occurence != 0:
                print str(i+1) + " occurs " + str(occurence) + " times"
            self.arr[i] = (self.arr[i] % maxEle) + 1

arr = [1,1,2,3,3,2,5]
frequenciesOfElements = FrequenciesOfElementsInPlace(arr)
frequenciesOfElements.findFrequencies()

