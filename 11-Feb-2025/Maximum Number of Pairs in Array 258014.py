# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        pair_count = 0
        non_pair_count = 0
        for count in freq_map.values():
            pair_count += count // 2
        
        non_pair_count = len(nums) - (pair_count * 2)
        return [pair_count, non_pair_count]

        