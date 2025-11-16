# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
        -10
    9       20
        15      7
    -10    -10    

    1
  /
  2  
/   \
3   4
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            ans = max(ans, leftMax + node.val + rightMax)
            return max(leftMax, rightMax) + node.val


        dfs(root)
        return ans
        