# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        maxHeap = []

        def dfs(node, maxHeap):
            if not node:
                return
            
            dfs(node.left, maxHeap)
            heapq.heappush(maxHeap, -node.val)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            dfs(node.right, maxHeap)

        dfs(root, maxHeap)

        return -maxHeap[0]

        