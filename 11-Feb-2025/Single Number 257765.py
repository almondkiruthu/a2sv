# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for num in nums:
            unique ^= num
        return unique
        