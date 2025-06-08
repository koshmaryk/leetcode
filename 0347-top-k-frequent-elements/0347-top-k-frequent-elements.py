from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
            
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        pq = []
        for key, val in freq.items():
            heapq.heappush(pq, (-val, key))

        output = []
        while k > 0:
            output.append(heapq.heappop(pq)[1])
            k -= 1
        return output