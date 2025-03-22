# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        for num in arr:
            distance = abs(num - x)
            heapq.heappush(minHeap, (distance, num))  # Store (distance, number)

        res = []
        # get the K smallest numbers.
        for pair in heapq.nsmallest(k, minHeap):
            res.append(pair[1])

        return sorted(res)