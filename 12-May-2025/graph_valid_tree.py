from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # A valid tree must have exactly n - 1 edges

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n

n = 5 
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
sol = Solution()
print(sol.validTree(n,edges))
