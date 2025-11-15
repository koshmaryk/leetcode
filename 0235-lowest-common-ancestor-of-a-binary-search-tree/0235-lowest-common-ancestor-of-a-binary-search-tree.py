# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if max(p.val, q.val) < curr.val:
                curr = curr.left
            elif min(p.val, q.val) > curr.val:
                curr = curr.right
            else:
                return curr