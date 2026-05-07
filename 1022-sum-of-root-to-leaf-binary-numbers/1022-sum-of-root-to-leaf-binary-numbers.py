# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_num):
            if not node:
                return 0

            curr_num = (curr_num << 1) | node.val
            if not node.left and not node.right:
                return curr_num
            
            return dfs(node.left, curr_num) + dfs(node.right, curr_num)

        return dfs(root, 0)