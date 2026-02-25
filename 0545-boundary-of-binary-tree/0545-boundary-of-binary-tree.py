# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left = []
        def left_dfs(node):
            if not node:
                return

            if node.left or node.right:
                left.append(node.val)

            if node.left:
                left_dfs(node.left)
            else:
                left_dfs(node.right)

        leaves = []
        def leaves_dfs(node):
            if not node.left and not node.right:
                leaves.append(node.val)
                return

            if node.left:
                leaves_dfs(node.left)
            if node.right:
                leaves_dfs(node.right)
            

        right = []
        def right_dfs(node):
            if not node:
                return

            if node.left or node.right:
                right.append(node.val)

            if node.right:
                right_dfs(node.right)
            else:
                right_dfs(node.left)

        answer = [root.val]

        left_dfs(root.left)
        answer.extend(left)

        if root.left or root.right:
            leaves_dfs(root)
        answer.extend(leaves)

        right_dfs(root.right)
        answer.extend(reversed(right))

        return answer

        