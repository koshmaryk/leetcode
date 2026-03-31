# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return output

        cols = defaultdict(list)
        min_col, max_col = 0, 0

        queue = deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            cols[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        for col in range(min_col, max_col + 1):
            output.append(cols[col])
        return output
