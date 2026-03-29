# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left = []
        def dfs_left(node):
            if not node:
                return

            if node.left or node.right:
                left.append(node.val)

            if node.left:
                dfs_left(node.left)
            else:
                dfs_left(node.right)

        leaves = []
        def dfs_leaves(node):
            if not node.left and not node.right:
                leaves.append(node.val)
                return

            if node.left:
                dfs_leaves(node.left)
            if node.right:
                dfs_leaves(node.right)
            

        right = []
        def dfs_right(node):
            if not node:
                return

            if node.left or node.right:
                right.append(node.val)

            if node.right:
                dfs_right(node.right)
            else:
                dfs_right(node.left)

        answer = [root.val]

        dfs_left(root.left)
        answer.extend(left)

        if root.left or root.right:
            dfs_leaves(root)
            answer.extend(leaves)

        dfs_right(root.right)
        answer.extend(reversed(right))

        return answer