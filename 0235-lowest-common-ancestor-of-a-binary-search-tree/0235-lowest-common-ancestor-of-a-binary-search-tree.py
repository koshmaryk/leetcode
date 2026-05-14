# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""

                7

            5       9

        3       6

    2      4

p = 6
q = 4


"""
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