class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # | |
        # A B A A
        # longest = 0
        # 3 < 4?
        longest = 0
        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            current_max = max(count.values()) # O(26)
            while r - l + 1 - current_max > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            if r - l + 1 - current_max <= k:
                longest = max(longest, r - l + 1)
        return longest