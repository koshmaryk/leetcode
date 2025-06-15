# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(x: Optional[TreeNode]):
            if x:
                values.append(x.val)
                traverse(x.left)
                traverse(x.right)

        values = []
        traverse(root)
        return values