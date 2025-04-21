# Problem: Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            # compute the left path cost and right path sum of the left and right subtrees

            # only take the positive contributions
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            self.max_total = max(self.max_total, node.val + left_sum + right_sum)

            return node.val + max(left_sum, right_sum)

        self.max_total = -math.inf
        dfs(root)

        return self.max_total
