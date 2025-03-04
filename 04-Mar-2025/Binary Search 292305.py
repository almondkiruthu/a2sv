# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0
        while left <= right:
            # calculate the middle
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1
        