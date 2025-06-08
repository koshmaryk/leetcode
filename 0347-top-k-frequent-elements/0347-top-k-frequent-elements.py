from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        pq = []
        for key, val in freq.items():
            heapq.heappush(pq, (val, key))

            if len(pq) > k:
                heapq.heappop(pq) 

        output = []
        while pq:
            output.append(heapq.heappop(pq)[1])
        return output