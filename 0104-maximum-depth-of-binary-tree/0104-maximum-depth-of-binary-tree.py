# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        ans = 0
        while stack:
            node, depth = stack.pop()
            if node:
                ans = max(ans, depth)
                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))
        return ans