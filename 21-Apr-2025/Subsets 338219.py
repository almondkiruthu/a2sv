# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        # start with the empty subset
        subsets.append([])
        for num in nums:
            # we take all the existing subsets and insert the current number
            # in them to create a new subset

            # the exisitig subsets we need to consider i.e the level size
            n = len(subsets)
            for i in range(n):
                # create a new subset from the existing subset and insert the current
                # element to it
                new_subset = list(subsets[i])
                new_subset.append(num)
                subsets.append(new_subset)
        
        return subsets
    