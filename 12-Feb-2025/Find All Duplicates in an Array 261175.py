# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            num = nums[i]
            correct_index_of_num = num - 1
            if num != nums[correct_index_of_num]:
                nums[i], nums[correct_index_of_num] = nums[correct_index_of_num], nums[i]
            else:
                i += 1
        duplicate_numbers = []
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                duplicate_numbers.append(nums[i])

        return duplicate_numbers