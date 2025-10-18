class Solution:
    from collections import defaultdict

    '''
    [1,2,2,3,4,1]

    [0,2,2,1,1,0]

    [0,0,1,1,2,2]
    '''
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        max_freq = max(freq.values())

        ans = 0
        for v in freq.values():
            if v == max_freq:
                ans += v
        return ans
        