# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while(i < n):
            num = nums[i]
            correct_index = num
            if num != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        res = []
        
        for i in range(n):
            if nums[i] != i:
                res.append(nums[i])

        return res
        