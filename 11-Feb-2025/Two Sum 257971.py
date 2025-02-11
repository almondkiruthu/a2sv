# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            num = nums[i]
            target_pair = target - num
            if target_pair in num_map:
                return [num_map[target_pair], i]
            num_map[num] = i