# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        cols = defaultdict(list)
        min_col, max_col = float('inf'), float('-inf')

        queue = deque([(root, 0)])
        while queue:
            for _ in range(len(queue)):
                curr, col = queue.popleft()

                min_col = min(min_col, col)
                max_col = max(max_col, col)

                cols[col].append(curr.val)
                if curr.left:
                    queue.append((curr.left, col - 1))
                if curr.right:
                    queue.append((curr.right, col + 1))

        output = []
        for key in range(min_col, max_col + 1):
            output.append(cols[key])
        return output