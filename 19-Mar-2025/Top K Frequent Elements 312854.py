# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []

        for i in range(k):
            heappush(minHeap, nums[i])


        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heappop(minHeap)
                heappush(minHeap, nums[i])

        return list(minHeap)
        