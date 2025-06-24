# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'), False)]
        while stack:
            node, min, max, visited = stack.pop()
            if node:
                if visited:
                    if not (min < node.val < max):
                        return False

                else:
                    stack.append((node.right, node.val, max, False))
                    stack.append((node, min, max, True))
                    stack.append((node.left, min, node.val, False))
        return True
