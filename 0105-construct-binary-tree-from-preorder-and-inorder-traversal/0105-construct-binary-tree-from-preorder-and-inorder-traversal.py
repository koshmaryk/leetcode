# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {node: i for i, node in enumerate(inorder)}

        pre_index = 0

        def dfs(l, r):
            nonlocal pre_index
            
            if l > r:
                return None

            root_val = preorder[pre_index]
            pre_index += 1
            root = TreeNode(root_val)

            mid = inorder_dict[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            
            return root

        return dfs(0, len(inorder) - 1)
        