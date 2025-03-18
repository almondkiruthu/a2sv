# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target == nums[mid]:
                return mid

            if nums[start] <= nums[mid]: # left side is sorted in ascending order.
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # right side is sorted in ascending order.
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        # not found in the array return -1
        return -1
        