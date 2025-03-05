# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # build the dynamic table
        dp = []
        for i in range(n + 1):
            row = []
            for j in range(m + 1):
                row.append(0)
            dp.append(row)
        
        for i in range(n):
            for j in range(m):
                if text2[i] == text1[j]:
                    # take the value that's diagonal which is r + 1 - 1 & c + 1 - 1 which same as dp[r][c]
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    # compare the prev row value and prev column value
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[n][m]