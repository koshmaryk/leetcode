from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        maxHeap = [-f for f in freq.values()]
        heapq.heapify(maxHeap)

        Q = deque() # (-count, idleTime)

        time = 0
        while maxHeap or Q:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    Q.append((count, time + n))

            if Q and Q[0][1] == time:
                heapq.heappush(maxHeap, Q.popleft()[0])

        return time