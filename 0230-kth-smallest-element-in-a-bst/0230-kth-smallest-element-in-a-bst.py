# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    heapq.heappush(pq, -node.val)
                    if len(pq) > k:
                        heapq.heappop(pq)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        
        return -pq[0]
        