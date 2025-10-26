# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {val:i for i,val in enumerate(inorder)}

        idx = 0

        def dfs(l, r):
            nonlocal idx
            if l > r:
                return None

            val = preorder[idx]
            idx += 1

            root = TreeNode(val)
            mid = lookup[val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root


        return dfs(0, len(inorder) - 1)
        