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


T(n) = T(1) * T(n - 2) + T(3) * T(n - 4) + .. + T(n - 2) * T(1)

'''
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def generate(n):
            trees = []
            if n % 2 == 0:
                return trees

            if n == 1:
                trees.append(TreeNode(0))
                return trees

            if n in memo:
                return memo[n]

            for root in range(1, n, 2):
                leftSubTree = generate(root)
                rightSubTree = generate(n - root - 1)

                for l in leftSubTree:
                    for r in rightSubTree:
                        trees.append(TreeNode(0, l, r))
            
            memo[n] = trees
            return trees

        return generate(n)