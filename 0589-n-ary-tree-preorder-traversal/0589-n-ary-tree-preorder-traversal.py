"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        values = []
        if not root:
            return values
            
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    values.append(node.val)
                else:
                    for child in node.children[::-1]:
                        stack.append((child, False))
                    stack.append((node, True))
        return values
