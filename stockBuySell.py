"""
The cost of a stock on each day is given in an array, find the max profit that you can make by
buying and selling in those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
the maximum profit can earned by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6.
If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
Time Complexity: O(n)
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

class StockBuySell(object):
    def __init__(self, inputArr):
        self.inputArr = inputArr
        self.inputArrLen = len(self.inputArr)
        self.count = 0

    def findMaxProfitPattern(self):
        if self.inputArrLen <= 1:
            return "Cannot be computed with the provided data"

        intervals = [Interval() for i in range(self.inputArrLen/2 +1+1)]

        i = 0
        while i < self.inputArrLen-1:

            # Find Local Minima. Note that the limit is (n-2) as we are
            # comparing present element to the next element.
            while i < self.inputArrLen-1 and self.inputArr[i] >= self.inputArr[i+1]:
                i += 1

            # If we reached the end, break as no further solution possible.
            if i == self.inputArrLen-1:
                break

            intervals[self.count].setBuy(i)
            i += 1

            # Find Local Maxima.  Note that the limit is (n-1) as we are
            # comparing to previous element
            while i < self.inputArrLen and self.inputArr[i] >= self.inputArr[i-1]:
                i += 1
            intervals[self.count].setSell(i-1)
            self.count += 1

        self.printPattern(intervals)

    def printPattern(self, intervals):
        for i in range(self.count):
            print "Buy on day " + str(intervals[i].getBuy()) + " and sell on " + str(intervals[i].getSell())

# Test
inputArr = [100, 180, 260, 310, 40, 535, 695]
stockBuySell = StockBuySell(inputArr)
stockBuySell.findMaxProfitPattern()