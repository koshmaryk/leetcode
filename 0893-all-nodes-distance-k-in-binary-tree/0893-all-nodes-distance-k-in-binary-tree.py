# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

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

        def dfs(u, d):
            if d == k:
                answer.append(u)
                return

            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    dfs(v, d + 1)

        dfs(target.val, 0)
        return answer
