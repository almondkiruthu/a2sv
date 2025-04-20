# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # The dfs algorithm returns the height not the diameter
        def dfs(node):
            if not node:
                return 0

            # get the both the left and right heights
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # only update if it's the longest path that we have seen so far
            self.res = max(self.res, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)

        return self.res
