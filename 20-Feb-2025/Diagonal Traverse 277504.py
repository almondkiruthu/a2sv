# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1:
            res = [num for row in mat for num in row]
            return res
        
        rows = len(mat)
        cols = len(mat[0])

        res = [deque([]) for _ in range(rows + cols - 1)]

        for row in range(rows):
            for col in range(cols):
                # we are at even index perform a positive diagonal traversal
                if (row + col) % 2 == 0:
                    res[row + col].appendleft(mat[row][col])
                else:
                    res[row + col].append(mat[row][col])
        
        return [num for row in res for num in row]

        