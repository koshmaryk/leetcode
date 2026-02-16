from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        pq = []
        for num,freq in counter.items():
            heapq.heappush(pq, (freq, num))

            if len(pq) > k:
                heapq.heappop(pq)
        
        ans = []
        while pq:
            _, num = heapq.heappop(pq)
            ans.append(num)
        return ans
    