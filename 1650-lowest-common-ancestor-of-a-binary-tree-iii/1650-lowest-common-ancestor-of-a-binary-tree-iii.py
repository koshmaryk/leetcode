"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

'''

        3
    p5       1q
2       4       6


5=1
6=2

step 1: p/q go up until min(d1, d2)
step 2: go up until p != q

'''

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def get_depth(x):
            depth = 0
            while x:
                x = x.parent
                depth += 1
            return depth


        p_depth = get_depth(p)
        q_depth = get_depth(q)

        for _ in range(p_depth - q_depth):
            p = p.parent
        
        for _ in range(q_depth - p_depth):
            q = q. parent

        while p != q:
            p = p.parent
            q = q.parent
        return p
        