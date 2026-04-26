from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        for f, t in edges:
            graph[f].append(t)
            indegree[t] += 1

        queue = deque(node for node in range(n) if indegree[node] == 0)

        ts = []
        while queue:
            node = queue.popleft()
            ts.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)

        ancestors = [set() for _ in range(n)]
        for node in ts:
            for next_node in graph[node]:
                ancestors[next_node].add(node)
                ancestors[next_node].update(ancestors[node])

        return [sorted(ancestors[i]) for i in range(n)]