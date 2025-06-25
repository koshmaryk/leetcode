# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root, root.val, False)]
        while stack:
            node, maximum, visited = stack.pop()
            if node:
                if visited:
                    if node.val >= maximum:
                        count += 1
                else:
                    maximum = max(maximum, node.val)
                    stack.append((node.right, maximum, False))
                    stack.append((node, maximum, True))
                    stack.append((node.left, maximum, False))
        return count