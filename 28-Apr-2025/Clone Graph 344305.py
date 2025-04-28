# Problem: Clone Graph - https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        visited = set()
        def dfs(node):
            if node in visited and node in old_to_new:
                return
            visited.add(node)
            new_node = Node(node.val)
            old_to_new[node] = new_node
            for neighbour in node.neighbors:
                dfs(neighbour)
        dfs(node)

        for old_node, new_node in old_to_new.items():
            new_node.neighbors = [old_to_new[neighbour] for neighbour in old_node.neighbors]
        
        return old_to_new[node]
        