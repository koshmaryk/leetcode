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

        s_path, d_path = [], []
        find_path(root, startValue, s_path)
        find_path(root, destValue, d_path)

        i = 0
        while i < len(s_path) and i < len(d_path) and s_path[i] == d_path[i]:
            i += 1

        return "U" * (len(s_path) - i) + "".join(d_path[i:])
