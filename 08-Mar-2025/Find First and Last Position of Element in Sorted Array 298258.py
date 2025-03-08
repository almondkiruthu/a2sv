# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # modified binary search helper function
        def binary_search(nums, target, findMaxIndex):
            target_index = -1
            start = 0
            end = len(nums) - 1
            
            while start <= end:
                mid = end - start // 2
                if target < nums[mid]:
                    end = mid - 1
                elif target > nums[mid]:
                    start = mid + 1
                else: # we found the target
                    target_index = mid
                    if findMaxIndex: # if we already found the first occurence of the target
                        start = mid + 1 # search ahead to find the last index of the target
                    else:
                        end = mid - 1 # search behind to find the first index of the target.
            return target_index

        res = [-1, -1]
        res[0] = binary_search(nums, target, False)
        if res[0] != -1:
            res[1] = binary_search(nums, target, True)
        return res

        