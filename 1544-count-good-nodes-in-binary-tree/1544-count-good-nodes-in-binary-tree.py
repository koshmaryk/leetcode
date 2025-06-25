# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        queue = deque([(root, root.val)])
        while queue:
            node, maximum = queue.popleft()
            if node.val >= maximum:
                count += 1
            
            maximum = max(maximum, node.val)
            if node.left:
                queue.append((node.left, maximum))
            if node.right:
                queue.append((node.right, maximum))
        return count