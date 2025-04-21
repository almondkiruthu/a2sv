# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node, arr):
            # only proceed if there is a node / root
            if not node:
                return arr
            queue = deque()
            queue.append(node)

            while len(queue) > 0:
                levelSize = len(queue)
                current_level = []
                for _ in range(levelSize):
                    curr_node = queue.popleft()
                    current_level.append(curr_node.val)

                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)

                arr.append(current_level[-1])

        res = []

        bfs(root, res)

        return res
        


