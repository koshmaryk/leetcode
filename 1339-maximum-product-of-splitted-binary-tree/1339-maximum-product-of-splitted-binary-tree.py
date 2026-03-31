# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def get_total_sum(node):
            if not node:
                return 0

            return get_total_sum(node.left) + node.val + get_total_sum(node.right)

        total_sum = get_total_sum(root)

        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            tree_sum = dfs(node.left) + node.val + dfs(node.right)
            ans = max(ans, (total_sum - tree_sum) * tree_sum)
            return tree_sum

        dfs(root)
        return ans % (10**9 + 7)