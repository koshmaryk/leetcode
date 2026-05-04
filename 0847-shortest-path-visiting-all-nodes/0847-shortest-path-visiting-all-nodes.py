from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        all_seen = frozenset(range(n))

        queue = deque()
        visited = set()

        for i in range(n):
            state = (i, frozenset([i]))
            queue.append((0, state))
            visited.add(state)

        while queue:
            steps, (node, seen) = queue.popleft()

            if seen == all_seen:
                return steps

            for next_node in graph[node]:
                new_seen = seen | frozenset([next_node])
                state = (next_node, new_seen)
                if state not in visited:
                    queue.append((steps + 1, state))
                    visited.add(state)
        return -1


