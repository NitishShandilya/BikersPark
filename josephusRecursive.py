"""
With n people standing in a circle, on every iteration the kth person is removed.
Find the person who won't be removed in the end.
"""
class josephusRecursive:
    def findSafePosition(self, numOfPeople, eliminatorPosition):
        self.numPeople = numOfPeople
        self.iterativeEliminator = eliminatorPosition
        if self.numPeople == 1:
            return 1
        else:
            return (self.findSafePosition(numOfPeople - 1, eliminatorPosition) + eliminatorPosition - 1) % numOfPeople + 1

#Test
josephus = josephusRecursive()
numOfPeople = 14
eliminatorPosition = 2
print josephus.findSafePosition(numOfPeople, eliminatorPosition)