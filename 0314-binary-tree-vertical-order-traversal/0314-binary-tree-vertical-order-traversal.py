# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        def dfs(node, row, col):
            if node:
                nonlocal min_col, max_col
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                cols[col].append((row, node.val))
        
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        min_col, max_col = float('inf'), float('-inf')
        cols = defaultdict(list) # Space Complexity O(n)
        dfs(root, 0, 0) # Time Complexity O(n), Space Complexity O(log n) - O(n)

        output = []
        for key in range(min_col, max_col + 1): # Time Complexity O(n)
            cols[key].sort(key=lambda x:x[0]) # Time Complexity O(n log n)
            output.append([val for _,val in cols[key]])  # Time Complexity O(n)
        return output
