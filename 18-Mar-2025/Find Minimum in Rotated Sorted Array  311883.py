# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        rotation_count = 0

        while start < end:
            mid = start + (end - start) // 2

            # if mid is greater than the next element.
            if mid < end and nums[mid] > nums[mid + 1]: # if it return a truthy value return true.
                rotation_count = max(rotation_count, mid + 1)
            
            # if mid is smaller than the previous element>
            if mid > start and nums[mid - 1] > nums[mid]:
                rotation_count = max(rotation_count, mid)

            
            if nums[start] < nums[mid]: # left side is sorted, so the pivot is on the right side
                start = mid + 1
            else: # right side is sorted and the pivot is on the left side.
                end = mid - 1
        

        if rotation_count > 0:
            return min(sorted(nums))
        else:
            return min(nums)