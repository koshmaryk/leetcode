# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

                3
    9                       20
NIL NIL               15            7
                    NIL NIL      NIL NIL

'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {v:i for i,v in enumerate(inorder)}
        
        pre_index = 0

        def build(l, r):
            nonlocal pre_index

            if l > r:
                return None

            root_val = preorder[pre_index]
            pre_index += 1
            root = TreeNode(root_val)

            mid = lookup[root_val]
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(inorder) - 1)
