# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heights = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    left_height, right_height = heights.get(node.left, 0), heights.get(node.right, 0)
                    if abs(left_height - right_height) > 1:
                        return False

                    heights[node] = 1 + max(left_height, right_height)
                else:
                    stack.append((node, True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))
        return True