# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth, col):
            if node:
                nonlocal ans
                if depth not in leftmost:
                    leftmost[depth] = col

                ans = max(ans, col - leftmost[depth] + 1)

                dfs(node.left, depth + 1, 2 * col)
                dfs(node.right, depth + 1, 2 * col + 1)

        leftmost = {}
        ans = 0

        dfs(root, 0, 0)
        return ans

