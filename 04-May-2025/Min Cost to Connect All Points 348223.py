# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        min_cost = 0
        seen = set()

        # intiliaze the minheap with the distance and node
        minHeap = [(0, 0)]

        while minHeap:
            weight, vertex = heapq.heappop(minHeap)
            if vertex not in seen:
                seen.add(vertex)
                min_cost += weight
                xi, yi = points[vertex]
                # from this specific source explore every other destination
                for j in range(len(points)):
                    if j not in seen:
                        xj, yj = points[j]
                        heapq.heappush(minHeap, (abs(xi - xj) + abs(yi - yj), j))

        return min_cost


        