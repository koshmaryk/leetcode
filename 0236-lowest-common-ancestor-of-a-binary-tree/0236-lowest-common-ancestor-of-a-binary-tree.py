# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    case 1: p == q
    case 2: p is LCA of q or vice versa
    case 3: x is LCA of p and q
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        queue = deque([root])
        while p not in parent or q not in parent:
            curr = queue.popleft()
            if curr.left:
                parent[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                queue.append(curr.right)

        s = set()
        while p:
            s.add(p)
            p = parent[p]

        while q not in s:
            q = parent[q]

        return q