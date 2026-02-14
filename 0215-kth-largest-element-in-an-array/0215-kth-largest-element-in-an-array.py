import heapq

'''
k=3

[3,2,1,5,6,4]

[6,5,4,3,2,1]
ans = 4
k = 0
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, -num)

        ans = float('inf')
        while k > 0:
            ans = -heapq.heappop(pq)
            k -= 1
        return ans
        