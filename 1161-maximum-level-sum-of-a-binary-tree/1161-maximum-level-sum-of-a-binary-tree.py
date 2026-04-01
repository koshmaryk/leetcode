# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maximum = float('-inf')
        ans = 1

        level = 1
        queue = deque([root])
        while queue:
            level_size = len(queue)
            curr = 0
            for _ in range(level_size):
                node = queue.popleft()
                curr += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curr > maximum:
                maximum = curr
                ans = level

            level += 1
        return ans
