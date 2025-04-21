# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(node, arr):
            # only proceed if there is a node
            if not node:
                return arr
            
            queue = deque()
            queue.append(node)

            while len(queue) > 0:
                level_size = len(queue)
                current_level = []
                for _ in range(level_size):
                    curr_node = queue.popleft()
                    # add the node to the current level
                    current_level.append(curr_node.val)
                    # insert the children of current_node in the queue.
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)

                arr.append(current_level)

        bfs(root, res)

        return res