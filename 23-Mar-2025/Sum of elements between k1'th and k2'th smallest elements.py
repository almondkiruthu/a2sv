import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        minHeap = []
        for num in A:
            heapq.heappush(minHeap, num)
            
        for _ in range(K1):
            heapq.heappop(minHeap)

        total = 0
        
        for _ in range(K2 - K1 - 1):
            total += heapq.heappop(minHeap)

        return total
