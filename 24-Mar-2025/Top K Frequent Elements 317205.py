# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            heappush(heap, (val, key))

            if len(heap) > k:
                # remove the most smallest element to remain with 
                # the most frequent K elements.
                heappop(heap)

                
        # Time complexity is 0(n log k)

        return [h[1] for h in heap]

        