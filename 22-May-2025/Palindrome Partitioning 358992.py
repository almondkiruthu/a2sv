# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []

        def backtrack(i):
            if i == len(s):
                res.append(sol.copy())
                return

            for j in range(i, len(s)):
                # if curr substring is a palindrome
                sub_string = s[i:j+1]
                if sub_string[::-1] == sub_string:
                    sol.append(sub_string)
                    backtrack(j + 1)
                    sol.pop()
        
        backtrack(0)
        return res
        