# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_sums = []
        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            tree_sum = left_sum + node.val + right_sum
            tree_sums.append(tree_sum)
            return tree_sum

        total_sum = dfs(root)

        ans = 0
        for tree_sum in tree_sums:
            ans = max(ans, (total_sum - tree_sum) * tree_sum)
        return ans % (10**9 + 7)