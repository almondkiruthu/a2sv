# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:  
        maxHeap = []
        for x, y in points:
            distance = -(x ** 2 +  y ** 2) # use negative distance for maxheap
            heapq.heappush(maxHeap, (distance, [x, y]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [closest_points[1] for closest_points in maxHeap]
        