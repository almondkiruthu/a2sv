# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums) - 1
        for i in range(n):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            else:
                continue
    
        res = [0] * len(nums)

        # a pointer for the index of res
        res_index = 0

        for num in nums:
            # if num is not falsy i.e non zero element
            if num:
                res[res_index] = num
                res_index += 1

        return res
