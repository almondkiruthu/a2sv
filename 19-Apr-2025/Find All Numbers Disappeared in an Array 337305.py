# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            num = nums[i]
            correct_num_index = num - 1
            # if the num is not in it's correct position swap else continue
            if num != nums[correct_num_index]:
                nums[i], nums[correct_num_index] = nums[correct_num_index], nums[i]
            else:
                i += 1

        res = []

        for i in range(len(nums)):
            if i != nums[i] - 1:
                res.append(i + 1)

        return res
