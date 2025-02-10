# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = {}
        for a in nums1:
            for b in nums2:
                sum = a + b
                if sum in sum_map:
                    sum_map[sum] += 1
                else:
                    sum_map[sum] = 1
        # Accumulate the number of times the current sum of pairs from nums3 and nums4
        # when added to the pair sums of nums1 and nums2 gives zero i.e.. sum to zero
        count = 0
        for c in nums3:
            for d in nums4:
                # Target is the negative of the pair sum c, d which would give zero when added to a pair sum from num1 and nums2
                target = -(c + d)
                if target in sum_map:
                    count += sum_map[target]
        return count