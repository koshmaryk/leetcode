# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
ans = 4

target = 1

        1

    -1       3

1   5           -3   

curr = 3


"""
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0

        counts = defaultdict(int)
        counts[0] = 1

        def explore(node, currSum):
            nonlocal ans
            if not node:
                return

            currSum += node.val
            ans += counts[currSum - targetSum]

            counts[currSum] += 1

            explore(node.left, currSum)
            explore(node.right, currSum)

            counts[currSum] -= 1

        explore(root, 0)
        return ans
        