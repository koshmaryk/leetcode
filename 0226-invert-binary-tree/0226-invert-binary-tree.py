# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        Q = deque([root])
        while Q:
            node = Q.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        return root
        