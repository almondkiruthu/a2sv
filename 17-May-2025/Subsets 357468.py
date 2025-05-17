# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # BFS approach
        subsets = []
        subsets.append([])

        for num in nums:
            n = len(subsets)
            for i in range(n):
                new_set = list(subsets[i])
                new_set.append(num)
                subsets.append(new_set)

        return subsets