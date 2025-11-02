# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
#   1,2,3,4,5
#   1   2   3,4,5
#   1   2   3   4,5
#         3 4   5       
#           
#
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def generate(leftmost, rightmost):
            trees = []
            if leftmost > rightmost:
                trees.append(None)
                return trees

            if (leftmost, rightmost) in memo:
                return memo[(leftmost, rightmost)]

            for root in range(leftmost, rightmost + 1):
                leftSubTree = generate(leftmost, root - 1)
                rightSubTree = generate(root + 1, rightmost)

                for left in leftSubTree:
                    for right in rightSubTree:
                        trees.append(TreeNode(root, left, right))

            memo[(leftmost, rightmost)] = trees
            return trees

        return generate(1, n)