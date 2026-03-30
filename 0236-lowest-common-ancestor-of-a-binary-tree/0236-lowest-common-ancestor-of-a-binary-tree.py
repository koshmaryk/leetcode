# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    '''
    case 1: p == q
    case 2: p is LCA of q or vice versa
    case 2: x is LCA of p and q


            3

        4       5

    5     6         7


    p = 7
    q = 4

    p = 4
    q = 6

    p = 4
    q = 4

    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left_tree = self.lowestCommonAncestor(root.left, p, q)
        right_tree = self.lowestCommonAncestor(root.right, p, q)

        if left_tree and right_tree:
            return root

        return left_tree if left_tree else right_tree 
        