# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sol =  []

        def backtrack():
            if len(sol) == len(nums):
                ans.append(sol.copy())

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()

        return ans
        