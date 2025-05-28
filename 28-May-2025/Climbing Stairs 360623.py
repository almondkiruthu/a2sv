# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


        # ----- dfs with memoization  
        # cache = {}
        # def dfs(i):
        #     if i == n:
        #         return 1
        #     elif i > n:
        #         return 0
            
        #     # memoization if i in cache then we have already calculated the ways from this step "i"
        #     if i in cache:
        #         return cache[i]
        #     # Recursive step: The number of ways to reach "n" from starting point i
        #     # Is the sum of ways to reach n from the i + 1 branch and i + 2 branch
        #     path_count = dfs(i + 1) + dfs(i + 2)
        #     cache[i] = path_count
        #     return path_count

        # return dfs(0)