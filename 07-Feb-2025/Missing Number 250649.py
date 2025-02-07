# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            num = nums[i]
            position = i
            if num != position:
                return position
        return len(nums)