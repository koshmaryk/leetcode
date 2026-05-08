"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 0
        stack = [(root, 1)]
        while stack:
            node, curr_depth = stack.pop()
            if node:
                depth = max(depth, curr_depth)
                for child in node.children:
                    stack.append((child, curr_depth + 1))
        return depth
