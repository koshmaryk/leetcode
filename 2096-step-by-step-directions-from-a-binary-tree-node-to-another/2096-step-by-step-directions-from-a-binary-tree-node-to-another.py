# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
s=3 t=6


            5
    1               2

3               6       4

LL
RL


"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node, startValue, destValue):
            if not node or node.val in [startValue, destValue]:
                return node

            left = lca(node.left, startValue, destValue)
            right = lca(node.right, startValue, destValue)

            return node if left and right else left or right


        def find_path(node, value, path):
            if not node:
                return False
            if node.val == value:
                return True
            for direction, child in [("L", node.left), ("R", node.right)]:
                path.append(direction)
                if find_path(child, value, path):
                    return True
                path.pop()
            return False

        ancestor = lca(root, startValue, destValue)

        s_path, d_path = [], []
        find_path(ancestor, startValue, s_path)
        find_path(ancestor, destValue, d_path)

        return "U" * len(s_path) + "".join(d_path)
