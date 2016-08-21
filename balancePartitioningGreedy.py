"""
Balance partitioning using greedy algorithm assuming that the array is sorted in decreasing order.
"""
class balancePartitioningGreedy:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def partitionMinimumSum(self):
        c1 = self.arr[0]
        c2 = self.arr[1]
        for i in range(2,self.length):
            if c1 > c2:
                c2 += self.arr[i]
            else:
                c1 += self.arr[i]

        minSum = None
        if c1 > c2:
            minSum = c1 - c2
        else:
            minSum = c2 - c1

        return minSum

arr = [50,16,15,14,13,12]
balance = balancePartitioningGreedy(arr)
print balance.partitionMinimumSum()