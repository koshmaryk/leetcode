# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
            4
        2       5
    1      3

2
t=6
l=1
r=3

5 * 1
5*1=5

3 * 3
3*3=9


1


'''
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def get_total(node):
            if not node:
                return 0
            return get_total(node.left) + node.val + get_total(node.right)

        total = get_total(root)

        ans = 0 
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            subtree_sum = dfs(node.left) + node.val + dfs(node.right)
            ans = max(ans, (total - subtree_sum) * subtree_sum)
            return subtree_sum
        
        dfs(root)
        return ans % (10**9 + 7)
