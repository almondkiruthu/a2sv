# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Iterate over each element in the matrix starting from the second row and second column
        # because the comparison starts with the element just above and to the left (i-1, j-1).
        for i in range(1, rows):
            for j in range(1, cols):
                # Compare the current element with the element diagonally above and to the left.
                # If any such comparison fails, the matrix is not Toeplitz.
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True