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
        queue = deque([(root, 0)])
        while queue:
            for _ in range(len(queue)):
                curr, col = queue.popleft()
                cols[col].append(curr.val)
                if curr.left:
                    queue.append((curr.left, col - 1))
                if curr.right:
                    queue.append((curr.right, col + 1))

        output = []
        for key in sorted(cols.keys()): # x = log n; x log x
            output.append(cols[key])
        return output