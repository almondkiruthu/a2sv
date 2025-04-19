# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        rows = m
        cols = n

        if len(original) != (rows * cols):
            return []

        matrix = []
        for k in range(rows):
            start = k * cols
            end = (k + 1) * cols
            row = original[start:end]
            matrix.append(row)
        
        return matrix