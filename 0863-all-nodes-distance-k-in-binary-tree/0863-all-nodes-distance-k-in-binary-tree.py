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
                graph[node].append(parent)
                graph[parent].append(node)
            
            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)

        build_graph(root, None)

        answer = []
        visited = set()

        def dfs(node, dist):
            if not node:
                return

            visited.add(node)

            if dist == k:
                answer.append(node.val)
                return

            for next_node in graph[node]:
                if next_node not in visited:
                    dfs(next_node, dist + 1)

        dfs(target, 0)
        return answer


        