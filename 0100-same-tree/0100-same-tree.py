# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            curr1, curr2 = queue.popleft()

            if not curr1 and not curr2:
                continue

            if not curr1 or not curr2:
                return False

            if curr1.val != curr2.val:
                return False

            queue.append((curr1.left, curr2.left))
            queue.append((curr1.right, curr2.right))

        return True
        