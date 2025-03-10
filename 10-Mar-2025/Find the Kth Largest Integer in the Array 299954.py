# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        unique_nums = [int(num) for num in nums]
        unique_nums = sorted(list(unique_nums), reverse=True)
        
        if len(unique_nums) >= k:
            return str(unique_nums[k - 1])
        