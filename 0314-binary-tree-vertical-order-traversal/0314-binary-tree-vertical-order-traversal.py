# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return output

        cols = defaultdict(list)
        min_col, max_col = float('inf'), float('-inf')

        def dfs(node, row, col):
            nonlocal min_col, max_col
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            cols[col].append((row, node.val))

            if node.left:
                dfs(node.left, row + 1, col - 1)
            if node.right:
                dfs(node.right, row + 1, col + 1)
            
        dfs(root, 0, 0)

        for col in range(min_col, max_col + 1):
            cols[col].sort(key=lambda x:x[0])
            vals = []
            for _, val in cols[col]:
                vals.append(val)
            output.append(vals)
        return output
