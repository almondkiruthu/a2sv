# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {nums[i]:i for i in range(len(nums))}
        for i in range(len(operations)):
            operation = operations[i]
            num_to_replace, query = operation
            # obtain the index of the value we are going to change
            idx = d[num_to_replace]
            nums[idx] = query
            d[query] = idx

        return nums