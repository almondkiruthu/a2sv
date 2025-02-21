# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_pos = []
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_pos.append([row, col])

        for row, col in zero_pos:
            # set the rows to zero
            for i in range(cols):
                matrix[row][i] = 0
            
            # set the entire column to zero
            for i in range(rows):
                matrix[i][col] = 0