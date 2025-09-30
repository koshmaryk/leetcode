# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def dfs(node, number): # 4 | 49 & 40 | - & 495,491
            nonlocal total_sum
            if not node.left and not node.right:
                total_sum += number # 40 + 495 + 491
                return

            if node.left:
                dfs(node.left, number * 10 + node.left.val) # 4 * 10 + 9 | 49 * 10 + 5
            if node.right:
                dfs(node.right, number * 10 + node.right.val) # 4 * 10 + 0 | 49 * 10 + 1

        dfs(root, root.val)
        return total_sum
        