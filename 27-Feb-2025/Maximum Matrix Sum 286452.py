# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        total_sum = 0
        negative_count = 0
        min_positive_value = float("inf")
        
        for row in range(n):
            for col in range(n):
                value = matrix[row][col]
                # add absolute value of the current element to the total_sum to obtain the highest possible
                # sum.
                total_sum += abs(value)

                # Record the minimum positive value(smallest abs value)
                min_positive_value = min(min_positive_value, abs(value))
                if value < 0:
                    negative_count += 1

        if negative_count % 2 == 0 or min_positive_value == 0:
            return total_sum
        else:
            # There's an odd number of negatives, subtract twice the minimum positive
            # value to account for the pair and the one value that will remain negative
            return total_sum - min_positive_value * 2


        