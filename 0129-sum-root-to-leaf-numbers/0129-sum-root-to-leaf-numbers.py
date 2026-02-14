# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    3
  2   1
5   0

325 + 320 + 31 = xxx

3 * 10 + 2 = 32

32 * 10 + 5 = 325

node 2 = 325 + 320
node 3 = 645 + 31

'''
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def dfs(node, number):
            nonlocal total
            if not node.left and not node.right:
                total += number
                return

            if node.left:
                dfs(node.left, number * 10 + node.left.val)
            if node.right:
                dfs(node.right, number * 10 + node.right.val)

        dfs(root, root.val)
        return total
