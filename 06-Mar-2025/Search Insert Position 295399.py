# Problem: Search Insert Position - https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)  
        left = 0
        right = n - 1

        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        # since the loop runs up to 'left <= right', so at the end of the while loop 'start == end + 1'
        # since right is decremented at some point
        # we are not able to find the target in nums array so the next big number will be at nums[left]
        return left
        
        