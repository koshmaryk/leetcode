from math import inf

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        cost = cnt = 0

        in_mst = [False] * n
        dist = [inf] * n
        dist[0] = 0

        while cnt < n:
            curr_weight = inf
            curr_node = -1

            # peak least weight node which is not in mst
            for node in range(n):
                if not in_mst[node] and curr_weight > dist[node]:
                    curr_weight = dist[node]
                    curr_node = node

            cost += curr_weight
            cnt += 1
            in_mst[curr_node] = True

            for next_node in range(n):
                weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])

                if not in_mst[next_node] and dist[next_node] > weight:
                    dist[next_node] = weight
        return cost
