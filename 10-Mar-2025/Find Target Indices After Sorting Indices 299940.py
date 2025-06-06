# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)

        left = 0
        right = len(nums) - 1
        res = []

        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        
        return res
        