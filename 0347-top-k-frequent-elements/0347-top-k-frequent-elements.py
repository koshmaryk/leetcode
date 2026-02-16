from collections import defaultdict

class Solution:
    '''
    1,1,2,2,3

    1:2, 2:2, 3:1

    [[],[3],[1,2],[],[],[]]

    k=3

    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        buckets = [[] for _ in range(n + 1)]
        for num,freq in counter.items():
            buckets[freq].append(num)

        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans      
        return ans
    