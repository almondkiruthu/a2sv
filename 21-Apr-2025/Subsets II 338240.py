# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort nums so that duplicates are next to each other
        nums = sorted(nums)
        subsets = []

        # start with the empty subset
        subsets.append([])

        start_index = end_index = 0
        for i in range(len(nums)):
            start_index = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start_index = end_index + 1
            end_index = len(subsets) - 1
            # obtain the level size or the number of iterations we need to perform
            # to form the new set from the existing subsets
            # the size is upto the end_index
            for j in range(start_index, end_index + 1):
                new_subset = list(subsets[j])
                new_subset.append(nums[i])
                subsets.append(new_subset)
        
        return subsets