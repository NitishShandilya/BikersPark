"""
The cost of a stock on each day is given in an array, find the max profit that you can make by
buying and selling in those days given k transactions.
The program uses Dynamic Programming and backtracking to print the transactions.
Time Complexity and Space Complexity is O(daysCount*k).
Since k can be at most daysCount, it's O(daysCount^2)
"""


class Interval(object):
    def __init__(self):
        self.buy = None
        self.sell = None
    def setBuy(self, buy):
        self.buy = buy
    def setSell(self, sell):
        self.sell = sell
    def getBuy(self):
        return self.buy
    def getSell(self):
        return self.sell

def maxProfit(values, k):
    valuesLen = len(values)
    dpArray = [[0 for _ in range(valuesLen)] for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, valuesLen):
            maxTransactionValue = 0
            for m in range(j):
                maxTransactionValue = \
                    max(maxTransactionValue, (values[j] - values[m] + dpArray[i - 1][m]))
                if maxTransactionValue < 0:
                    maxTransactionValue = 0
                    continue
            dpArray[i][j] = max(dpArray[i][j-1], maxTransactionValue)

    print("Maximum profit obtained is {maxProfit}".format(maxProfit=dpArray[-1][-1]))
    printInterval(dpArray, values)

def printInterval(dpArray, inputArr):
    k = len(dpArray) - 1
    day = len(dpArray[0]) - 1
    intervals = [Interval() for _ in range(k)]
    intervalCount = 0

    while True:
        if k == 0 or day == 0:
            break
        if dpArray[k][day] == dpArray[k][day-1]:
            day -= 1
        else:
            intervals[intervalCount].setSell(day)
            maxDiff = dpArray[k][day] - inputArr[day]
            for j in range(day, -1, -1):
                if dpArray[k-1][j] - inputArr[j] == maxDiff:
                    intervals[intervalCount].setBuy(j)
                    k -= 1
                    intervalCount += 1
                    break

    for interval in range(intervalCount-1,-1,-1):
        print("Buy on day {buy} and sell on {sell}"
              .format(buy=intervals[interval].getBuy(), sell=intervals[interval].getSell()))

# Test
inputArr = [2, 5, 7, 1, 4, 3, 1, 3]
k = 3
maxProfit(inputArr, 3)
