# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # create an (m + 1)*(n + 1) matrix - A
        A = []
        for i in range(n+1):
            row = []
            for j in range(m+1):
                row.append(i+j)
            A.append(row)
        for i in range(n):
            for j in range(m):
                A[i+1][j+1] = min (A[i][j+1] + 1, # deletion cost
                                    A[i+1][j] + 1, # insertion cost
                                    A[i][j] + int(word2[i] != word1[j]) #sub cost add 1 or 0 
                )
        return A[n][m]
        