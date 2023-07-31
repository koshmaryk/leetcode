# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is not None:
            stack.append((root, 1))

        maxDepth = 0
        while stack != []:
            node, depth = stack.pop()
            if node is not None:
                maxDepth = max(maxDepth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return maxDepth