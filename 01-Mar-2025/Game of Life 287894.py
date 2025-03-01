# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # Helper function to count live neighbors
        def count_live_neighbors(r, c):
            directions = [
                (-1, -1), (-1, 0), (-1, 1),  # Top three neighbors
                (0, -1), (0, 1),            # Left and right neighbors
                (1, -1), (1, 0), (1, 1)     # Bottom three neighbors
            ]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    count += 1
            return count

        # Step 1: Determine the next state using the encoding method
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)

                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1  # 1 -> 0
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2   # 0 -> 1

        # Step 2: Apply the transformations to update the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0  # Convert -1 back to 0
                elif board[r][c] == 2:
                    board[r][c] = 1  # Convert 2 back to 1
        