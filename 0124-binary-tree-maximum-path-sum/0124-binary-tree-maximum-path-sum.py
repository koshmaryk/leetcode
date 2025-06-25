# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def helper(node):
            nonlocal ans

            if not node:
                return 0

            leftMax = max(helper(node.left), 0)
            rightMax = max(helper(node.right), 0)

            ans = max(ans, leftMax + rightMax + node.val)
            return max(leftMax + node.val, rightMax + node.val)

        helper(root)
        return ans