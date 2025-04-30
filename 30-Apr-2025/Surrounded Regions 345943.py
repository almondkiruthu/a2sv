# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        # 1. (DFS) Capture the unsurrounded regions and convert them (o -> T)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row in [0, rows - 1] or col in [0, cols - 1]):
                    capture(row, col)
        # 2. capture surrounded regions and convert them to "X"
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
        # 2. uncapture unsurrounded regions and convert them form "T" to "O"
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"




        # for col in range(cols):
        #     # we have found an unsurrounded zero on the border
        #     if board[0][col] == "O":
        #         board[0][col] = "T"
        # for row in range(1, rows):
        #     if board[row][0] == "O":
        #         board[row][0] = "T"
        # for col in range(1, cols):
        #     if board[rows - 1][col] == "O":
        #         board[rows - 1][col] = "T"
        # for row in range(1, rows - 1):
        #     if board[row][cols - 1] == "O":
        #         board[row][cols - 1] = "T"