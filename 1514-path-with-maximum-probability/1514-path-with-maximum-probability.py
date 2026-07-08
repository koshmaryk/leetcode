from collections import defaultdict, deque


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u,v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        in_queue = [False] * n
        in_queue[start_node] = True

        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            in_queue[node] = False

            for next_node, next_prob in graph[node]:
                if max_prob[node] * next_prob > max_prob[next_node]:
                    max_prob[next_node] = max_prob[node] * next_prob
                    if not in_queue[next_node]:
                        queue.append(next_node)
                        in_queue[next_node] = True

        return max_prob[end_node]
                    

      

                

        