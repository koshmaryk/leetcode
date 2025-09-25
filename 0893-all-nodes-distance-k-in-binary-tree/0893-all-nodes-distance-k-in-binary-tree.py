# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(node, parent):
            if node and parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)

        build_graph(root, None)

        answer = []
        visited = set([target.val])

        queue = deque([(target.val, 0)])
        while queue:
            u, d = queue.popleft()

            if d == k:
                answer.append(u)
                continue

            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append((v, d + 1))

        return answer