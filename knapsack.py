"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
"""
class Knapsack(object):
    def __init__(self, number_of_items, total_weight, values_list, weights_list):
        self.number_of_items = number_of_items
        self.weight = total_weight
        self.values_list = values_list
        self.weights_list = weights_list
        self.dpArray = [[ 0 for i in range(self.weight+1)] for j in range(self.number_of_items+1)]

    def find_max_weight(self):
        for i in range(1,self.number_of_items+1):
            for j in range(1,self.weight+1):
                if self.weights_list[i-1] > j:
                    self.dpArray[i][j] = self.dpArray[i-1][j]
                else:
                    self.dpArray[i][j] = \
                        max(self.dpArray[i-1][j], self.values_list[i-1] + self.dpArray[i-1][j-self.weights_list[i-1]])
        #print self.dpArray
        return self.dpArray[self.number_of_items][self.weight]


number_of_items = 3
total_weight = 50
values_list = [60, 100, 120]
weights_list = [10,20,30]
knapsack = Knapsack(number_of_items, total_weight, values_list, weights_list)
print knapsack.find_max_weight()