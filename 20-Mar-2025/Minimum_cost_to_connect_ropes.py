from typing import List
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
        # code here
        minHeap = []
        for rope in arr:
            heapq.heappush(minHeap, rope)
            
        res = 0
        curr_connection = 0
        
        while len(minHeap) > 1:
            curr_connection = heapq.heappop(minHeap) + heapq.heappop(minHeap)
            
            res += curr_connection
            heapq.heappush(minHeap, curr_connection)
            
        return res
