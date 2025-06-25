# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node

        parent = None
        curr = root
        while curr:
            parent = curr
            if node.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

        return root