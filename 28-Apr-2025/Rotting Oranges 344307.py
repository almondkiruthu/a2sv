# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows = len(grid)
        cols = len(grid[0])

        num_fresh = 0
        queue = deque()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == FRESH:
                    num_fresh += 1
                elif grid[row][col] == ROTTEN:
                    queue.append((row, col))

        if num_fresh == 0:
            return 0
        
        num_of_minutes = -1
        while queue:
            queue_size = len(queue)
            num_of_minutes += 1
            for _ in range(queue_size):
                row, col = queue.popleft()

                directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    n_row = row + dr
                    n_col = col + dc

                    if (n_row >= 0 and n_row < rows and n_col >= 0 and n_col < cols and 
                        grid[n_row][n_col] == FRESH):
                        grid[n_row][n_col] = ROTTEN
                        num_fresh -= 1
                        queue.append((n_row, n_col))
        

        return num_of_minutes if num_fresh == 0 else -1