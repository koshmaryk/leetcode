"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def helper(node: Optional['Node']):
            if not node:
                return node

            if node in visited:
                return visited[node]

            cloneNode = Node(node.val)

            visited[node] = cloneNode

            for neighbor in node.neighbors:
                cloneNode.neighbors.append(helper(neighbor))

            return cloneNode

        return helper(node)