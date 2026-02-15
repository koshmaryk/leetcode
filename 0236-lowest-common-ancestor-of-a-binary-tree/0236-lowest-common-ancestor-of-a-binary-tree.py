# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    '''
    case 1: p == q
    case 2: p is LCA of q or vice versa
    case 3: x is LCA of p and q

            3
        5       1
    6       2       7
8       4

p=4
q=2

6->4; 6->8; 5->6; 5->2; 3->5; 1->7; 3->1

set = [4, 6, 5, 3]



    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        queue = deque([root])
        while p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q
        