from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        buckets = [[] for _ in range(n + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        output = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
        return output