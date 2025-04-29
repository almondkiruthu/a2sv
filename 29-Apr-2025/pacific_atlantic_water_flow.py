class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        rows = len(heights)
        cols = len(heights[0])

        # top row
        for col in range(cols):
            p_queue.append((0, col))
            p_seen.add((0, col))
        
        # left row excluding the top left
        for row in range(1, rows):
            p_queue.append((row, 0))
            p_seen.add((row, 0))

        # right row
        for row in range(rows):
            a_queue.append((row, cols - 1))
            a_seen.add((row, cols - 1))
        
        # bottom row excluding the bottom right
        for col in range(cols - 1):
            a_queue.append((rows - 1, col))
            a_seen.add((rows - 1, col))

        def get_coords(queue, seen):
            coords = set()

            while queue:
                r, c = queue.popleft()
                coords.add((r, c))

                neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in neighbours:
                    n_r = r + dr
                    n_c = c + dc
                    # check if the neighbour position is within bounds and the neighbour
                    # can flow water to us i.e. they are bigger or equal to the current coordinate
                    if (0 <= n_r < rows and 0 <= n_c < cols and
                        heights[n_r][n_c] >= heights[r][c] and (n_r, n_c) not in seen):

                        seen.add((n_r, n_c))
                        queue.append((n_r, n_c))
                

            return coords

        p_coords = get_coords(p_queue, p_seen)
        a_coords = get_coords(a_queue, a_seen)

        return list(p_coords.intersection(a_coords))
