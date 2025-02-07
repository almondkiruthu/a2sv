# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        for key in freq_map:
            value = freq_map[key]
            if value > n / 2:
                return key