# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visit = set()

        def backtrack(row, col, i):
            # Successful case
            if i == len(word):
                return True
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                (row, col) in visit or
                board[row][col] != word[i]):
                return False
            
            visit.add((row, col))
            neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in neighbours:
                nr = row + dr
                nc = col + dc
                if backtrack(nr, nc, i + 1):
                    return True

            visit.remove((row, col))

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
        