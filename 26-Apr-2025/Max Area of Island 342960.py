# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = []

        def dfs(row, col, visited):
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or
                grid[row][col] == 0 or
                (row, col) in visited):

                return 0
            
            visited.add((row, col))
            
            area = 1

            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                n_row = row + dr
                n_col = col + dc  
                area += dfs(n_row, n_col, visited)

            
            return area

        max_area = float("-inf")
        for row in range(rows):
            for col in range(cols):
                    # run a dfs search on every cell on the grid
                    curr_area = 0
                    curr_area = (dfs(row, col, visited))
                    max_area = max(max_area, curr_area)

        return max_area
