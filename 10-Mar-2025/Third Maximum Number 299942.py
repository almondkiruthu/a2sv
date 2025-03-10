# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = sorted(list(set(nums)))
        unique_nums = unique_nums[::-1]

        if len(unique_nums) >= 3:
            return unique_nums[2]
        else:
            return unique_nums[0]

        