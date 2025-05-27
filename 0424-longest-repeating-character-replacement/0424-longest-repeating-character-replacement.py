class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # | |
        # A B A A
        # longest = 0
        # 3 < 4?
        ans = 0
        count = {}
        max_freq = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
