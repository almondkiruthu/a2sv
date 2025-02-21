# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # loop through the range from left to right + 1 since it's included
        for num in range(left, right + 1):
           # check if any num in the ranges is not in any of the sub ranges and if so return false
           if not any(start <= num <= end for start, end in ranges):
                return False
        
        # if every digit/num is covered
        return True