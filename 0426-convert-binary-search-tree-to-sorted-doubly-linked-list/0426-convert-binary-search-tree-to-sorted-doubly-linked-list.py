"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    '''
        2
    1       3


    head = 1
    prev = 3

    1<->2<->3<->1

    stack = []
    
    '''
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        prev = None
        head = None

        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if not prev:
                        head = node
                    else:
                        prev.right = node
                        node.left = prev
                    prev = node
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        
        prev.right = head
        head.left = prev
        return head
        