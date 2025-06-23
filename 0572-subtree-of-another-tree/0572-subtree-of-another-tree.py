# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(q, p):
            queue = deque([(q, p)])
            while queue:
                node1, node2 = queue.popleft()

                if not node1 and not node2:
                    continue
                
                if not node1 or not node2:
                    return False

                if node1.val != node2.val:
                    return False

                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            return True

        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False