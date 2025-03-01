# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = {}
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                value = board[row][col]
                neighbours = []
                if row - 1 > -1 and col - 1 > -1:
                    neighbours.append(board[row - 1][col - 1])
                if row - 1 > -1:
                     neighbours.append(board[row - 1][col])
                if row - 1 > - 1 and col + 1 < cols:
                     neighbours.append(board[row - 1][col + 1])
                if col - 1 > -1:
                     neighbours.append(board[row][col - 1])
                if col + 1 < cols:
                     neighbours.append(board[row][col + 1])
                if row + 1 < rows and col - 1 > -1:
                     neighbours.append(board[row + 1][col - 1])
                if row + 1 < rows:
                     neighbours.append(board[row + 1][col])
                if row + 1 < rows and col + 1 < cols:
                     neighbours.append(board[row + 1][col + 1])

                    
                neighbours_size = len(neighbours)
                counter = Counter(neighbours)

                if value == 1 and counter[1] < 2:
                    d[(row, col)] = 0
                elif value == 1 and (counter[1] == 2 or counter [1] == 3):
                    d[(row, col)] = 1
                elif value == 1 and counter[1] > 3:
                    d[(row, col)] = 0
                elif value == 0 and counter[1] == 3:
                    d[(row, col)] = 1
        
        for key in d:
            row, col = key
            new_value = d[key]
            board[row][col] = new_value
        