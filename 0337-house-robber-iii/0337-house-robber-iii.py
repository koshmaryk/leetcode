# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
     3                    [3]
    / \             /           \
   2   3          [3,2]        [1,3]
    \   \           \            \
     3   1        [0,3]        [0,1]
                   / \          / \
                [0,0] [0,0]  [0,0] [0,0]
'''
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def helper(root):
            if not root:
                return 0

            if root in memo:
                return memo[root]

            rob_curr = root.val
            if root.left:
                rob_curr += helper(root.left.left) + helper(root.left.right)
            if root.right:
                rob_curr += helper(root.right.left) + helper(root.right.right)

            not_rob_curr = helper(root.left) + helper(root.right)
            memo[root] = max(rob_curr, not_rob_curr)
            return memo[root]
        
        return helper(root)