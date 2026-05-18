from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        max_freq = 0
        count = defaultdict(int)
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
