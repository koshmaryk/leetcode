# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0, 0 # sum, cnt

            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)

            node_sum, node_cnt = l_sum + r_sum + node.val, l_cnt + r_cnt + 1
            if node_sum // node_cnt == node.val:
                ans += 1

            return node_sum, node_cnt

        dfs(root)
        return ans