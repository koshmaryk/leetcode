# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_node(node, target):
            if not node or node == target:
                return node

            left = find_node(node.left, target)
            right = find_node(node.right, target)

            return left or right


        def lca(node, p, q):
            if not node or node == p or node == q:
                return node

            left = lca(node.left, p, q)
            right = lca(node.right, p, q)

            return node if left and right else left or right
            

        p_node = find_node(root, p)
        q_node = find_node(root, q)

        if not p_node or not q_node:
            return None

        return lca(root, p, q)
