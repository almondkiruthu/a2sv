# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # The tree is balanced if the left and right sub-trees are balanced and diff
            # between the left and right subtrees is less than or equal to 1
            balanced = (left_height[0] and right_height[0] 
                        and abs(left_height[1] - right_height[1]) <= 1)

            return (balanced, 1 + max(left_height[1], right_height[1]))

        return dfs(root)[0]