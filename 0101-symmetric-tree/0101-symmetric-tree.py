# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.popleft()
                tmp.append(node.val if node else float('inf'))


                if node:
                    queue.append(node.left)
                    queue.append(node.right)

            l, r = 0, size - 1
            while l < r:
                if tmp[l] != tmp[r]:
                    return False
                l += 1
                r -= 1
        return True