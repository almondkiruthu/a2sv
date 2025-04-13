# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        maxHeap = []
        for row in range(n):
            for col in range(n):
                val = matrix[row][col]

                heapq.heappush(maxHeap, -val)

                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)

        return -heapq.heappop(maxHeap)