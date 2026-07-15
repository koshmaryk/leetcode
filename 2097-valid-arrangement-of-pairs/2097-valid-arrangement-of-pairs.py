from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree, out_degree = defaultdict(int), defaultdict(int)
        for s,e in pairs:
            graph[s].append(e)
            out_degree[s] += 1
            in_degree[e] += 1

        start = -1
        for node in out_degree:
            if out_degree[node] == in_degree[node] + 1:
                start = node
                break

        path = []
        def visit(node):
            while graph[node]:
                visit(graph[node].pop())
            path.append(node)

        visit(pairs[0][0] if start == -1 else start)
        
        path = path[::-1]

        result = []
        for i in range(len(path) - 1):
            result.append([path[i], path[i + 1]])
        return result
