from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = []

        graph = defaultdict(list)
        for f,t in sorted(tickets, reverse=True):
            graph[f].append(t)

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]
