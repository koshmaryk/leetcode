# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
            1
        3       3
    3       2   null null
null null null null

Ideas:
 - if not curr.left and not curr.right and curr.val == target: return TreeNode(0)
 - if left == TreeNode(0) or right == TreeNode(0): curr.left/curr.right = None

'''
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root
