# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subsets = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                subsets.append(subset.copy())
                return

            #Left side pick
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            
            #Right side don't pick
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        
        backtrack(0)

        return subsets