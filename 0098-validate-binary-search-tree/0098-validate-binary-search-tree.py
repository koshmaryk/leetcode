# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            node, min, max = queue.popleft()
            if not (min < node.val < max):
                return False
            
            if node.left:
                queue.append((node.left, min, node.val))
            if node.right:
                queue.append((node.right, node.val, max))
        return True