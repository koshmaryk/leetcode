
from collections import defaultdict

class Solution:
    #   | |
    # p w w k e w
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans