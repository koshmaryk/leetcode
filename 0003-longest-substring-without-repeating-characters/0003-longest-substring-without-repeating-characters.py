class Solution:
    #   | |
    # p w w k e w
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while seen[s[r]] > 1:
                seen[s[l]] = seen.get(s[l], 0) - 1
                l +=1
            ans = max(ans, r - l + 1)
        return ans