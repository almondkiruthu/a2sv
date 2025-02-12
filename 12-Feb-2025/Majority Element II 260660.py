# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
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
            if value > n / 3:
                res.append(key)

        return res