# Problem: Smallest Range Covering Elements from K Lists - https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import math
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        rangeStart, rangeEnd = 0, math.inf
        curr_max_num = -math.inf

        for arr in nums:
            heapq.heappush(minHeap, (arr[0], 0, arr))
            curr_max_num = max(curr_max_num, arr[0])

        while len(minHeap) == len(nums):
            num, i, arr = heapq.heappop(minHeap)
            if rangeEnd - rangeStart > curr_max_num - num:
                rangeStart = num
                rangeEnd = curr_max_num
            
            if len(arr) > i + 1:
                heapq.heappush(minHeap, (arr[i+1], i+1, arr))
                curr_max_num = max(curr_max_num, arr[i+1])

        return [rangeStart, rangeEnd]