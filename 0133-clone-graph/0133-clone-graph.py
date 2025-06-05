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
        if not node:
            return node

        Q, visited = deque([node]), {node: Node(node.val)}
        while Q:
            curr_node = Q.popleft()
            curr_clone = visited[curr_node]

            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    Q.append(neighbor)
            
                curr_clone.neighbors.append(visited[neighbor])

        return visited[node]
            