# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# -2,-1,0,1,2
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque([(root, 0)])
        while queue:
            _, head_index = queue[0]
            _, tail_index = queue[-1]
            for _ in range(len(queue)):
                node, col = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * col))
                if node.right:
                    queue.append((node.right, 2 * col + 1))
            ans = max(ans, tail_index - head_index + 1)
        return ans
        