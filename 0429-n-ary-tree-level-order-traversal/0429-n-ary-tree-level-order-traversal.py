"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        values = []
        if not root:
            return values

        def dfs(node, level):
            if len(values) == level:
                values.append([])

            values[level].append(node.val)
            for child in node.children:
                dfs(child, level + 1)

        dfs(root, 0)
        return values
