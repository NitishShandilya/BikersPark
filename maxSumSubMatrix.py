"""
Given a 2D array or matrix, find the sub-matrix that gives the maximum sum.
The algorithm utilizies Kadane's algorithm and Dynamic programming mashup.
The idea is to fix the left and right columns one by one and find the
maximum sum contiguous rows using Kadane's algorithm for every left and right column pair.
If the sum is more than a global value of sum, then update the left and right columns and
update top and bottom values by the maximum sum fetching top and bottom values obtained from Kadane's algorithm.
Time complexity is O(m*m*n), where m in the number of columns and n is the number of rows in the matrix.
"""
INT_MIN = -32676
class MaxSumSubMatrix(object):
    def __init__(self, matrix, rows, cols):
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        self.dpArray = [0]*self.rows

    def findMaxSumKadane(self, arr):
        max_sum = INT_MIN
        temp_sum = start_index = temp_start = 0
        end_index = -1
        for i in range(len(arr)):
            temp_sum += arr[i]
            if temp_sum < 0:
                temp_sum = 0
                temp_start = i+1
            elif temp_sum > max_sum:
                max_sum = temp_sum
                start_index = temp_start
                end_index = i

        # At least 1 non-negative element
        if end_index != -1:
            return max_sum, start_index, end_index

        # All negative elements
        max_sum = arr[0]
        start_index = end_index = 0
        for i in range(1,len(arr)):
            if arr[i] > max_sum:
                max_sum = arr[i]
                start_index = end_index = i
        return max_sum, start_index, end_index

    def findMaxSumSubMatrix(self):
        final_top = final_bottom = final_left = final_right = 0
        max_sum = INT_MIN
        for left in range(self.cols):
            self.dpArray = [0]*self.rows
            print "row" + str(left)
            for right in range(left,self.cols):
                print "col" + str(right)
                for i in range(self.rows):
                    self.dpArray[i] += self.matrix[i][right]

                elements_returned = self.findMaxSumKadane(self.dpArray)
                curr_sum = elements_returned[0]
                curr_top = elements_returned[1]
                curr_bottom = elements_returned[2]
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    final_top = curr_top
                    final_bottom = curr_bottom
                    final_left = left
                    final_right = right

        return (max_sum, final_top, final_left, final_bottom, final_right)


# Test
matrix = [[1, 2, -1, -4, -20],[-8, -3, 4, 2, 1],[3, 8, 10, 1, 3],[-4, -1, 1, 7, -6]]
rows = 4
cols = 5
maxSumSubMatrix = MaxSumSubMatrix(matrix, rows, cols)
print maxSumSubMatrix.findMaxSumSubMatrix()