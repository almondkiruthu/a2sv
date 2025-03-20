# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heappush(heap, (val, key))
            else:
                heappushpop(heap, (val, key))

        return [h[1] for h in heap]

        