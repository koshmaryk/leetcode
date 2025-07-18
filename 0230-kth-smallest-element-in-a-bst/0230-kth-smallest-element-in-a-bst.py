# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1

        def dfs(node):
            nonlocal ans, k
            if not node:
                return

            dfs(node.left)
            k -= 1
            if k == 0:
                ans = node.val
                return
            dfs(node.right)

        dfs(root)

        return ans