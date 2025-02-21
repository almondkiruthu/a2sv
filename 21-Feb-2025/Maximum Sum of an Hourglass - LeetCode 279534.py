# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        hourglass = 0
        for row in range(rows - 2): # stop 2 rows before the end to form a valid trio
            for col in range(cols - 2): # stop 2 cols before the end to form a valid trio of cols
                curr_hourglass = 0
                upper_bound = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
                middle_bound = grid[row + 1][col + 1]
                lower_bound = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]

                curr_hourglass = upper_bound + middle_bound + lower_bound

                hourglass = max(hourglass, curr_hourglass)
        
        return hourglass
        