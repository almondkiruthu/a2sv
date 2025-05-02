class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [(grid[0][0], 0, 0)] #time/maxHeight, r, c
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        visit.add((0, 0))

        while minHeap:
            time, row, col = heapq.heappop(minHeap)
            
            if row == n - 1 and col == n - 1:
                return time
            
            for dr, dc in directions:
                neiR, neiC, = row + dr, col + dc

                if (neiR < 0 or neiC < 0 or neiR >= n or neiC >= n
                    or (neiR, neiC) in visit):
                    continue
                else:
                    visit.add((neiR, neiC))
                    heapq.heappush(minHeap, (max(time, grid[neiR][neiC]), neiR, neiC))
