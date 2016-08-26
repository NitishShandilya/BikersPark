"""
Given identical eggs and access to a multi-storey building.
The aim is to find out the minimum number of trials in the worst case to find the
threshold floor from which an egg will break when dropped out of a window from that floor.
If an egg is dropped and does not break, it is undamaged and can be dropped again.
However, once an egg is broken, we cannot reuse the egg.
"""
INT_MAX = 32767
class EggDrop(object):
    def __init__(self, floors, eggs):
        self.floors = floors
        self.eggs = eggs
        self.dpArray = [[0 for i in range(self.floors+1)] for i in range(self.eggs+1)]

    def findMinDrops(self):
        if self.floors == 0:
            return self.floors
        if self.eggs == 1:
            return self.floors

        for i in range(self.floors+1):
            self.dpArray[1][i] = i

        for j in range(self.eggs+1):
            self.dpArray[j][1] = 1

        for i in range(2,self.eggs+1):
            for j in range(2,self.floors+1):
                self.dpArray[i][j] = INT_MAX
                for k in range(1,j+1):
                    self.dpArray[i][j] = min(self.dpArray[i][j], 1+max(self.dpArray[i-1][k-1], self.dpArray[i][j-k]))

        return self.dpArray[self.eggs][self.floors]

#Test
floors = 100
eggs = 2
eggDrop = EggDrop(floors, eggs)
print eggDrop.findMinDrops()