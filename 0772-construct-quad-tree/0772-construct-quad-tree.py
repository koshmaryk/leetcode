"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(n, r, c):
            if n == 1:
                return Node(grid[r][c], True)

            n = n // 2
            topLeft = helper(n, r, c)
            topRight = helper(n, r, c + n)
            bottomLeft = helper(n, r + n, c)
            bottomRight = helper(n, r + n, c + n)

            if (topLeft.isLeaf 
                and topRight.isLeaf
                and bottomLeft.isLeaf
                and bottomRight.isLeaf
                and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return topLeft

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return helper(len(grid), 0, 0)

        