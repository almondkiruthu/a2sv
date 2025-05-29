# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        n = len(cost)
        cache = {}
        def dfs(i):
            total = 0
            if i >= n:
                return 0 # No cost after the top

            if i in cache:
                return cache[i]
            
            one_step_cost = dfs(i + 1)
            two_steps_cost = dfs(i + 2)
            total = cost[i] + min(one_step_cost, two_steps_cost)
            # print(f"I have added {cost[i]} and one step {one_step_cost} and two step cost {two_steps_cost}")
            cache[i] = total
            return total
        
        return min(dfs(0), dfs(1))
        