# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            # count the current node and then take the max number of nodes
            # of it's left and right children
            left_child_nodes = dfs(node.left)
            right_child_nodes = dfs(node.right)

            return 1 + max(left_child_nodes, right_child_nodes)

            
        return dfs(root)