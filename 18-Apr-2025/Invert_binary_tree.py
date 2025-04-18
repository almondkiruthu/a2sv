# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            queue = deque()
            queue.append(node)
            while len(queue) > 0:
                level_size = len(queue)
                for _ in range(level_size):
                    curr_node = queue.popleft()
                    temp = curr_node.left
                    curr_node.left = curr_node.right
                    curr_node.right = temp
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
        # call bfs with root.
        if root:
            bfs(root)
            return root
