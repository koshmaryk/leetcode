# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    1 2 3 4 5

    1

   2  3

  4 5

'''
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        trees = []
        if n % 2 == 0:
            return trees

        if n == 1:
            trees.append(TreeNode())
            return trees

        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)

            for l in left:
                for r in right:
                    trees.append(TreeNode(0, l, r))
        return trees
