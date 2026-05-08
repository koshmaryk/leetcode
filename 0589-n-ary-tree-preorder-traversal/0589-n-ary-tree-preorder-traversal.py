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
            
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                values.append(node.val)
                for child in node.children[::-1]:
                    stack.append(child)
        return values
