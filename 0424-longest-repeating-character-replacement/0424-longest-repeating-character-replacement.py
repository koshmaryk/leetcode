class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # | |
        # A B A A
        # longest = 0
        # 3 < 4?
        ans = 0
        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
